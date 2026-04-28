import tkinter as tk
from tkinter import ttk
from app.utils.style import Theme

class BillingView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Fee Management & Billing")
        self.geometry("600x400")
        self.configure(bg=Theme.BG_COLOR)
        
        self._build_ui()

    def _build_ui(self):
        ttk.Label(self, text="Billing & Fee Management", style="Title.TLabel").pack(pady=20)
        ttk.Label(self, text="Feature coming soon...", style="Header.TLabel").pack(pady=20)
        
        ttk.Button(self, text="Close", command=self.destroy).pack(pady=20)
