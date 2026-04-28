from app.services.db_manager import DatabaseManager
from app.models.student import Student
import mysql.connector

class StudentService:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def create_student(self, student: Student):
        conn = self.db_manager.get_connection()
        if not conn: return False
        
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO students (first_name, last_name, dob, grade, contact_number) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (student.first_name, student.last_name, student.dob, student.grade, student.contact_number))
            conn.commit()
            return cursor.lastrowid
        except mysql.connector.Error as e:
            print(f"Error creating student: {e}")
            return False
        finally:
            if 'cursor' in locals(): cursor.close()

    def get_all_students(self):
        conn = self.db_manager.get_connection()
        if not conn: return []
        
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM students")
            results = cursor.fetchall()
            return [Student(r['id'], r['first_name'], r['last_name'], r['dob'], r['grade'], r['contact_number']) for r in results]
        except mysql.connector.Error as e:
            print(f"Error fetching students: {e}")
            return []
        finally:
            if 'cursor' in locals(): cursor.close()

    def update_student(self, student: Student):
        conn = self.db_manager.get_connection()
        if not conn: return False
        
        try:
            cursor = conn.cursor()
            query = """
                UPDATE students 
                SET first_name=%s, last_name=%s, dob=%s, grade=%s, contact_number=%s 
                WHERE id=%s
            """
            cursor.execute(query, (student.first_name, student.last_name, student.dob, student.grade, student.contact_number, student.student_id))
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error updating student: {e}")
            return False
        finally:
            if 'cursor' in locals(): cursor.close()

    def delete_student(self, student_id: int):
        conn = self.db_manager.get_connection()
        if not conn: return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error deleting student: {e}")
            return False
        finally:
            if 'cursor' in locals(): cursor.close()
