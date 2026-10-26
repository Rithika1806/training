from fastapi import FastAPI, HTTPException
from models import Student
from repository import StudentRepository

app= FastAPI(
    title="Student Marks Service (SMS)",
    version="1.0"
)

repo=StudentRepository() #repository object

#HOME
@app.get("/")
def home():
    return{"message":"Student Marks Service(SMS)"}

#Create a student
@app.post("/students",response_model=Student)
def create_student(student:Student):
    try:
        return repo.create(student)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
#Read all
@app.get("/students",response_model=list[Student])
def get_students():
    return repo.get_all()

#Read by id
@app.get("/students/{student_id}",response_model=Student)
def get_student(student_id:int):
    student=repo.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

#update by id
@app.put("/students/{student_id}",response_model=Student)
def update_student(student_id:int, student:Student):
    updated=repo.update(student_id,student)
    if updated is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

#delete by id
@app.delete("/students/student_id")
def delete_student(student_id:int):
    deleted=repo.delete(student_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message":"Student deleted successfully"}