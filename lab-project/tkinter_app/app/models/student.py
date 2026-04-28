class Student:
    def __init__(self, student_id=None, first_name="", last_name="", dob=None, grade="", contact_number=""):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.grade = grade
        self.contact_number = contact_number

    def __repr__(self):
        return f"<Student(id={self.student_id}, name={self.first_name} {self.last_name})>"
