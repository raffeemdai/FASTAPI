from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Student Management API",
    description="Practice CRUD operations using FastAPI",
    version="1.0"
)

# --------------------------------------------------
# Pydantic Model
# --------------------------------------------------

class Student(BaseModel):
    id: int
    name: str
    department: str
    cgpa: float


# --------------------------------------------------
# Sample Data
# --------------------------------------------------

students = [
    {
        "id": 1,
        "name": "Ananya",
        "department": "CSE",
        "cgpa": 8.9
    },
    {
        "id": 2,
        "name": "Rahul",
        "department": "ECE",
        "cgpa": 8.4
    },
    {
        "id": 3,
        "name": "Priya",
        "department": "IT",
        "cgpa": 9.1
    }
]


# --------------------------------------------------
# Home Route
# --------------------------------------------------

@app.get("/")
def home():
    return {"message": "Student Management API Running"}


# --------------------------------------------------
# GET ALL STUDENTS
# --------------------------------------------------

@app.get("/students")
def get_all_students():
    return students


# --------------------------------------------------
# GET STUDENT BY ID
# Path Parameter Example
# --------------------------------------------------

@app.get("/student/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# --------------------------------------------------
# FILTER BY DEPARTMENT
# Query Parameter Example
# --------------------------------------------------

@app.get("/students/filter")
def filter_students(department: str):

    result = [
        student
        for student in students
        if student["department"].lower() == department.lower()
    ]

    return result


# --------------------------------------------------
# CREATE STUDENT
# POST
# --------------------------------------------------

@app.post("/student")
def create_student(student: Student):

    for existing_student in students:
        if existing_student["id"] == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student.model_dump())

    return {
        "message": "Student added successfully",
        "student": student
    }


# --------------------------------------------------
# UPDATE STUDENT
# PUT
# --------------------------------------------------

@app.put("/student/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student
):

    for index, student in enumerate(students):

        if student["id"] == student_id:
            students[index] = updated_student.model_dump()

            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# --------------------------------------------------
# DELETE STUDENT
# DELETE
# --------------------------------------------------

@app.delete("/student/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student["id"] == student_id:
            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
