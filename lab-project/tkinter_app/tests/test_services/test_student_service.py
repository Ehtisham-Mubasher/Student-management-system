import pytest
from unittest.mock import MagicMock, patch
from app.services.student_service import StudentService
from app.models.student import Student

@patch('app.services.student_service.DatabaseManager')
def test_create_student_success(MockDBManager):
    mock_db = MockDBManager.return_value
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_db.get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.lastrowid = 1

    student_service = StudentService()
    student = Student(first_name="John", last_name="Doe", dob="2010-01-01", grade="A", contact_number="123")
    result = student_service.create_student(student)
    
    assert result == 1
    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()

@patch('app.services.student_service.DatabaseManager')
def test_get_all_students(MockDBManager):
    mock_db = MockDBManager.return_value
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_db.get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'dob': '2010-01-01', 'grade': 'A', 'contact_number': '123'}
    ]

    student_service = StudentService()
    students = student_service.get_all_students()
    
    assert len(students) == 1
    assert isinstance(students[0], Student)
    assert students[0].first_name == "John"
