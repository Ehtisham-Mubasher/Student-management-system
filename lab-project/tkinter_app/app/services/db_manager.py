import mysql.connector
from mysql.connector import Error
import os

class DatabaseManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.connection = None
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "root"), # User to adjust as needed
                database=os.getenv("DB_NAME", "school_db")
            )
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            self._connect()
        return self.connection

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

def setup_database():
    """Create the database and tables if they don't exist."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "root")
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
            cursor.execute("USE school_db")
            
            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password_hash VARCHAR(255) NOT NULL,
                    role VARCHAR(50) DEFAULT 'admin'
                )
            """)
            
            # Create students table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    dob DATE,
                    grade VARCHAR(20),
                    contact_number VARCHAR(20)
                )
            """)
            
            # Seed default admin if no users exist
            cursor.execute("SELECT COUNT(*) FROM users")
            if cursor.fetchone()[0] == 0:
                # Password is 'admin123'
                cursor.execute("INSERT INTO users (username, password_hash, role) VALUES ('Admin', 'admin123', 'admin')")
            
            # Ensure the username is updated if it was previously created as 'admin'
            cursor.execute("UPDATE users SET username = 'Admin' WHERE username = 'admin'")
            
            conn.commit()
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Error setting up database: {e}")

if __name__ == "__main__":
    setup_database()
