from typing import Dict
from models import Student

class StudentRepository:
    #create an empty dictionary : 
    # where key is student id and value is corresponding Student object
    def __init__(self):
        self.students: Dict[int, Student] ={} 

    def create(self, student: Student):
        if student.id in self.students:
            raise ValueError("Student alreasy exists")
        self.students[student.id] = student
        return student
        
    def get(self, student_id: int):
        return self.students.get(student_id)
    
    def get_all(self):
        return list(self.students.values())
    
    def update(self, student_id:int, student: Student):
        if student_id not in self.students:
            return None
        self.students[student_id] =student
        return student
    
    def delete(self, student_id:int):
        return self.students.pop(student_id, None)