import tkinter as tk
from tkinter import ttk

class Theme:
    BG_COLOR = "#f4f5f7"
    PRIMARY_COLOR = "#4CAF50"
    SECONDARY_COLOR = "#2196F3"
    DANGER_COLOR = "#f44336"
    TEXT_COLOR = "#333333"
    WHITE = "#ffffff"

    FONT_TITLE = ("Helvetica", 20, "bold")
    FONT_HEADER = ("Helvetica", 14, "bold")
    FONT_BODY = ("Helvetica", 12)

def configure_styles():
    """Configure ttk styles for the application."""
    style = ttk.Style()
    
    # Check if a theme is available, try 'clam' for better styling
    if 'clam' in style.theme_names():
        style.theme_use('clam')

    # Common Styles
    style.configure("TFrame", background=Theme.BG_COLOR)
    style.configure("TLabel", background=Theme.BG_COLOR, foreground=Theme.TEXT_COLOR, font=Theme.FONT_BODY)
    style.configure("Title.TLabel", font=Theme.FONT_TITLE, foreground=Theme.PRIMARY_COLOR)
    style.configure("Header.TLabel", font=Theme.FONT_HEADER)

    # Button Styles
    style.configure("TButton", font=Theme.FONT_BODY, padding=6)
    style.configure("Primary.TButton", background=Theme.PRIMARY_COLOR, foreground=Theme.WHITE, font=("Helvetica", 12, "bold"))
    style.map("Primary.TButton", background=[("active", "#45a049")])

    style.configure("Secondary.TButton", background=Theme.SECONDARY_COLOR, foreground=Theme.WHITE, font=("Helvetica", 12, "bold"))
    style.map("Secondary.TButton", background=[("active", "#0b7dda")])

    style.configure("Danger.TButton", background=Theme.DANGER_COLOR, foreground=Theme.WHITE, font=("Helvetica", 12, "bold"))
    style.map("Danger.TButton", background=[("active", "#da190b")])

    # Entry Styles
    style.configure("TEntry", fieldbackground=Theme.WHITE, padding=5, font=Theme.FONT_BODY)
    
    # Treeview styles
    style.configure("Treeview", font=Theme.FONT_BODY, rowheight=25)
    style.configure("Treeview.Heading", font=Theme.FONT_HEADER, background=Theme.PRIMARY_COLOR, foreground=Theme.WHITE)

def center_window(window, width, height):
    """Utility to center a tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
