from app.services.db_manager import DatabaseManager
from app.models.user import User
import mysql.connector

class AuthService:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def authenticate(self, username, password):
        """
        Authenticate a user by username and password.
        Returns a User object if successful, None otherwise.
        """
        conn = self.db_manager.get_connection()
        if not conn:
            return None
            
        try:
            cursor = conn.cursor(dictionary=True)
            # Basic query, in a real app use hashed passwords!
            query = "SELECT * FROM users WHERE username = %s AND password_hash = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            
            if result:
                return User(
                    user_id=result['id'],
                    username=result['username'],
                    password_hash=result['password_hash'],
                    role=result['role']
                )
            return None
        except mysql.connector.Error as e:
            print(f"Auth error: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
