import pytest
import tkinter as tk
from unittest.mock import MagicMock
from app.views.dashboard import DashboardView

def test_dashboard_logout():
    root = tk.Tk()
    mock_user = MagicMock()
    mock_user.username = "test_user"
    mock_logout = MagicMock()
    
    view = DashboardView(root, user=mock_user, on_logout=mock_logout, on_open_students=MagicMock(), on_open_billing=MagicMock())
    
    view.on_logout()
    
    mock_logout.assert_called_once()
    root.destroy()
