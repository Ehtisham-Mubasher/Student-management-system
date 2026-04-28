import tkinter as tk
from tkinter import ttk, messagebox
from app.services.auth import AuthService
from app.utils.style import Theme, center_window

class LoginView(tk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent, bg=Theme.BG_COLOR)
        self.parent = parent
        self.on_login_success = on_login_success
        self.auth_service = AuthService()

        self._build_ui()

    def _build_ui(self):
        # Create a centered frame
        form_frame = ttk.Frame(self, padding=30, style="TFrame")
        form_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(form_frame, text="School Management System", style="Title.TLabel").grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(form_frame, text="Login to Continue", style="Header.TLabel").grid(row=1, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(form_frame, text="Username:").grid(row=2, column=0, sticky="e", pady=10, padx=5)
        self.username_var = tk.StringVar()
        self.entry_username = ttk.Entry(form_frame, textvariable=self.username_var, width=30)
        self.entry_username.grid(row=2, column=1, pady=10, padx=5)

        ttk.Label(form_frame, text="Password:").grid(row=3, column=0, sticky="e", pady=10, padx=5)
        self.password_var = tk.StringVar()
        self.entry_password = ttk.Entry(form_frame, textvariable=self.password_var, show="*", width=30)
        self.entry_password.grid(row=3, column=1, pady=10, padx=5)

        login_btn = ttk.Button(form_frame, text="Login", command=self.handle_login, style="Primary.TButton")
        login_btn.grid(row=4, column=0, columnspan=2, pady=20, ipadx=20)

    def handle_login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        user = self.auth_service.authenticate(username, password)
        if user:
            self.on_login_success(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
