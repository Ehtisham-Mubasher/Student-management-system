import tkinter as tk
from tkinter import ttk, messagebox
from app.services.student_service import StudentService
from app.models.student import Student
from app.utils.style import Theme

class StudentRegistrationView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Student Management")
        self.geometry("900x600")
        self.configure(bg=Theme.BG_COLOR)
        
        self.student_service = StudentService()
        self.selected_student_id = None

        self._build_ui()
        self.load_students()

    def _build_ui(self):
        # Top Title
        ttk.Label(self, text="Student Management (CRUD)", style="Title.TLabel").pack(pady=10)

        # Split into left form and right list
        main_frame = ttk.Frame(self, padding=10)
        main_frame.pack(fill="both", expand=True)

        # Left Form
        form_frame = ttk.LabelFrame(main_frame, text="Student Details", padding=10)
        form_frame.pack(side="left", fill="y", padx=10)

        ttk.Label(form_frame, text="First Name:").grid(row=0, column=0, sticky="e", pady=5)
        self.first_name_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.first_name_var).grid(row=0, column=1, pady=5)

        ttk.Label(form_frame, text="Last Name:").grid(row=1, column=0, sticky="e", pady=5)
        self.last_name_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.last_name_var).grid(row=1, column=1, pady=5)

        ttk.Label(form_frame, text="DOB (YYYY-MM-DD):").grid(row=2, column=0, sticky="e", pady=5)
        self.dob_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.dob_var).grid(row=2, column=1, pady=5)

        ttk.Label(form_frame, text="Grade:").grid(row=3, column=0, sticky="e", pady=5)
        self.grade_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.grade_var).grid(row=3, column=1, pady=5)

        ttk.Label(form_frame, text="Contact:").grid(row=4, column=0, sticky="e", pady=5)
        self.contact_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.contact_var).grid(row=4, column=1, pady=5)

        # Buttons
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Add", command=self.add_student, style="Primary.TButton").grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_student, style="Secondary.TButton").grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_student, style="Danger.TButton").grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_form).grid(row=1, column=1, padx=5, pady=5)

        # Right List
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(side="right", fill="both", expand=True)

        columns = ("id", "first_name", "last_name", "dob", "grade", "contact")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("first_name", text="First Name")
        self.tree.heading("last_name", text="Last Name")
        self.tree.heading("dob", text="DOB")
        self.tree.heading("grade", text="Grade")
        self.tree.heading("contact", text="Contact")

        self.tree.column("id", width=30)
        self.tree.column("grade", width=50)

        self.tree.pack(fill="both", expand=True, side="left")
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind('<<TreeviewSelect>>', self.on_select)

    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        students = self.student_service.get_all_students()
        for s in students:
            self.tree.insert("", tk.END, values=(s.student_id, s.first_name, s.last_name, s.dob, s.grade, s.contact_number))

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])['values']
            self.selected_student_id = values[0]
            self.first_name_var.set(values[1])
            self.last_name_var.set(values[2])
            self.dob_var.set(values[3])
            self.grade_var.set(values[4])
            self.contact_var.set(values[5])

    def clear_form(self):
        self.selected_student_id = None
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.dob_var.set("")
        self.grade_var.set("")
        self.contact_var.set("")
        self.tree.selection_remove(self.tree.selection())

    def get_form_data(self):
        return Student(
            student_id=self.selected_student_id,
            first_name=self.first_name_var.get().strip(),
            last_name=self.last_name_var.get().strip(),
            dob=self.dob_var.get().strip() or None,
            grade=self.grade_var.get().strip(),
            contact_number=self.contact_var.get().strip()
        )

    def add_student(self):
        student = self.get_form_data()
        if not student.first_name or not student.last_name:
            messagebox.showwarning("Validation", "First and Last Name are required.")
            return
            
        result = self.student_service.create_student(student)
        if result:
            messagebox.showinfo("Success", "Student added successfully.")
            self.clear_form()
            self.load_students()
        else:
            messagebox.showerror("Error", "Failed to add student. Check format/database.")

    def update_student(self):
        if not self.selected_student_id:
            messagebox.showwarning("Selection", "Please select a student to update.")
            return
            
        student = self.get_form_data()
        if self.student_service.update_student(student):
            messagebox.showinfo("Success", "Student updated successfully.")
            self.load_students()
        else:
            messagebox.showerror("Error", "Failed to update student.")

    def delete_student(self):
        if not self.selected_student_id:
            messagebox.showwarning("Selection", "Please select a student to delete.")
            return
            
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            if self.student_service.delete_student(self.selected_student_id):
                messagebox.showinfo("Success", "Student deleted successfully.")
                self.clear_form()
                self.load_students()
            else:
                messagebox.showerror("Error", "Failed to delete student.")
