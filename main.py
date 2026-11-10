from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Management System", description="A simple API for managing student records", version="1.0.0")

#temp data storage

students={
    1:{
        "name":"John Doe",
        "age":20,
        "grade":"A"
    },
    2:{
        "name":"Jane Doe",
        "age":21,
        "grade":"B"
    }
}

#Request data verification model
class Student(BaseModel):
    name:str
    age:int
    grade:str

#Get student details-GET method
@app.get("/student")
def get_students():
    return students 

#Get student details by id-GET method
@app.get("/student/{student_id}")
def get_student(student_id:int):
    if student_id in students:
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")

#Add student details-POST method
@app.post("/student",status_code=201)
def add_student(student: Student):
    new_id = max(students.keys()) + 1 
    students[new_id] = student.model_dump()
    return{
        "id":new_id,
        "student": students[new_id]
    }

#Update student details-PUT method
@app.put("/student/{student_id}")
def update_student(student_id:int,student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student.model_dump()
    return{
        "id":student_id,
        "student":students[student_id]
    }

#Delete student details-DELETE method
@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return{
        "message":f"Student with id {student_id} has been deleted"
    }