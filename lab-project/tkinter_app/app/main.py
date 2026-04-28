import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from app.views.login import LoginView
from app.views.dashboard import DashboardView
from app.views.student_registration import StudentRegistrationView
from app.views.billing import BillingView
from app.utils.style import configure_styles, center_window, Theme
from app.services.db_manager import setup_database

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School Management System")
        self.geometry("400x500")
        self.configure(bg=Theme.BG_COLOR)
        
        # Configure global styles
        configure_styles()
        center_window(self, 400, 500)
        
        self.current_user = None
        self.current_frame = None

        self.show_login()

    def switch_frame(self, frame_class, *args, **kwargs):
        """Destroys current frame and replaces it with a new one."""
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, *args, **kwargs)
        self.current_frame.pack(fill="both", expand=True)

    def show_login(self):
        self.geometry("400x500")
        center_window(self, 400, 500)
        self.switch_frame(LoginView, on_login_success=self.handle_login_success)

    def handle_login_success(self, user):
        self.current_user = user
        self.geometry("800x600")
        center_window(self, 800, 600)
        self.switch_frame(
            DashboardView, 
            user=self.current_user,
            on_logout=self.handle_logout,
            on_open_students=self.open_students_window,
            on_open_billing=self.open_billing_window
        )

    def handle_logout(self):
        self.current_user = None
        self.show_login()

    def open_students_window(self):
        StudentRegistrationView(self)

    def open_billing_window(self):
        BillingView(self)

if __name__ == "__main__":
    # Ensure database is set up before starting the app
    setup_database()
    app = Application()
    app.mainloop()
