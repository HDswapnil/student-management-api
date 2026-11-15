
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from models.student import Student as StudentModel
from schemas.student import StudentCreate, StudentRead


app = FastAPI(
    title="Student Management System",
    description="A simple API for managing student records",
    version="1.0.0"
)


# CREATE - Add a new student
@app.post(
    "/students",
    response_model=StudentRead,
    status_code=201
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = StudentModel(
        name=student.name,
        age=student.age,
        grade=student.grade
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# READ - Retrieve all students
@app.get(
    "/students",
    response_model=list[StudentRead]
)
def get_students(db: Session = Depends(get_db)):

    students = db.query(StudentModel).all()

    return students


# READ - Retrieve a student by ID
@app.get(
    "/students/{student_id}",
    response_model=StudentRead
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(StudentModel).filter(
        StudentModel.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# UPDATE - Update student details
@app.put(
    "/students/{student_id}",
    response_model=StudentRead
)
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    existing_student = db.query(StudentModel).filter(
        StudentModel.id == student_id
    ).first()

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.grade = student.grade

    db.commit()
    db.refresh(existing_student)

    return existing_student


# DELETE - Delete a student
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(StudentModel).filter(
        StudentModel.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": f"Student with id {student_id} has been deleted"
    }
