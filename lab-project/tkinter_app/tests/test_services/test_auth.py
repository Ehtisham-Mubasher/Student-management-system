import pytest
from unittest.mock import MagicMock, patch
from app.services.auth import AuthService
from app.models.user import User

@patch('app.services.auth.DatabaseManager')
def test_authenticate_success(MockDBManager):
    # Setup mock
    mock_db = MockDBManager.return_value
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_db.get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    # Mock result from DB
    mock_cursor.fetchone.return_value = {
        'id': 1,
        'username': 'admin',
        'password_hash': 'admin123',
        'role': 'admin'
    }

    auth_service = AuthService()
    user = auth_service.authenticate('admin', 'admin123')
    
    assert user is not None
    assert isinstance(user, User)
    assert user.username == 'admin'

@patch('app.services.auth.DatabaseManager')
def test_authenticate_failure(MockDBManager):
    mock_db = MockDBManager.return_value
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_db.get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchone.return_value = None

    auth_service = AuthService()
    user = auth_service.authenticate('wrong', 'wrong')
    
    assert user is None
