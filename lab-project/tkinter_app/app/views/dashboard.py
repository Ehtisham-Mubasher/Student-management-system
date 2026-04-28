import tkinter as tk
from tkinter import ttk
from app.utils.style import Theme

class DashboardView(tk.Frame):
    def __init__(self, parent, user, on_logout, on_open_students, on_open_billing):
        super().__init__(parent, bg=Theme.BG_COLOR)
        self.parent = parent
        self.user = user
        self.on_logout = on_logout
        self.on_open_students = on_open_students
        self.on_open_billing = on_open_billing

        self._build_ui()

    def _build_ui(self):
        # Sidebar
        sidebar = ttk.Frame(self, style="TFrame")
        sidebar.pack(side="left", fill="y", padx=10, pady=10)

        # Main Content
        content = ttk.Frame(self, style="TFrame")
        content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # Sidebar items
        ttk.Label(sidebar, text=f"Welcome, {self.user.username}", style="Header.TLabel").pack(pady=20)

        ttk.Button(sidebar, text="Student Management", command=self.on_open_students, style="Secondary.TButton").pack(fill="x", pady=10)
        ttk.Button(sidebar, text="Fee / Billing", command=self.on_open_billing, style="Secondary.TButton").pack(fill="x", pady=10)
        
        # Spacer
        ttk.Frame(sidebar, style="TFrame").pack(fill="y", expand=True)
        
        ttk.Button(sidebar, text="Logout", command=self.on_logout, style="Danger.TButton").pack(fill="x", pady=20)

        # Content items
        ttk.Label(content, text="Dashboard Overview", style="Title.TLabel").pack(anchor="w", pady=(0, 20))
        
        # Dashboard cards/stats can go here
        stats_frame = ttk.Frame(content)
        stats_frame.pack(fill="x", pady=10)
        
        card1 = ttk.Frame(stats_frame, relief="raised", borderwidth=1, padding=20)
        card1.pack(side="left", padx=10, expand=True, fill="both")
        ttk.Label(card1, text="Total Students", style="Header.TLabel").pack()
        ttk.Label(card1, text="---", style="Title.TLabel").pack(pady=10)
