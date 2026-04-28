import pytest
import tkinter as tk
from unittest.mock import MagicMock, patch
from app.views.login import LoginView

@patch('app.views.login.AuthService')
def test_login_success(MockAuthService):
    mock_auth_service = MockAuthService.return_value
    mock_auth_service.authenticate.return_value = MagicMock() # Mock User
    
    root = tk.Tk()
    success_callback = MagicMock()
    
    view = LoginView(root, success_callback)
    view.username_var.set("admin")
    view.password_var.set("admin123")
    
    view.handle_login()
    
    mock_auth_service.authenticate.assert_called_with("admin", "admin123")
    success_callback.assert_called_once()
    root.destroy()

@patch('app.views.login.messagebox')
@patch('app.views.login.AuthService')
def test_login_failure(MockAuthService, mock_msgbox):
    mock_auth_service = MockAuthService.return_value
    mock_auth_service.authenticate.return_value = None # Failure
    
    root = tk.Tk()
    success_callback = MagicMock()
    
    view = LoginView(root, success_callback)
    view.username_var.set("wrong")
    view.password_var.set("wrong")
    
    view.handle_login()
    
    mock_auth_service.authenticate.assert_called_with("wrong", "wrong")
    success_callback.assert_not_called()
    mock_msgbox.showerror.assert_called_once()
    root.destroy()
