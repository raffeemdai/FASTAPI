# FastAPI CRUD Practice Guide
refer : https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-2-building-your-first-crud-api-lpl

## Overview

This project is based on a Student Management API built using FastAPI. It demonstrates:

- CRUD Operations (Create, Read, Update, Delete)
- Path Parameters
- Query Parameters
- Pydantic Models
- Request Validation
- Swagger API Documentation

Source Blog:
https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-2-building-your-first-crud-api-lpl

---

# Complete Code with Explanations

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
```

### Explanation

- FastAPI is the main framework.
- HTTPException is used for returning custom error responses.
- BaseModel is used by Pydantic to validate request data.

---

```python
app = FastAPI(
    title="Student Management API",
    description="Practice CRUD operations using FastAPI",
    version="1.0"
)
```

### Explanation

Creates a FastAPI application.

- title appears in Swagger UI.
- description explains the application.
- version tracks API versions.

---

## Student Model

```python
class Student(BaseModel):
    id: int
    name: str
    department: str
    cgpa: float
```

### Explanation

This is a Pydantic model.

It validates incoming request data.

Expected JSON:

```json
{
  "id": 1,
  "name": "Ananya",
  "department": "CSE",
  "cgpa": 8.9
}
```

FastAPI automatically checks:

- id must be integer
- name must be string
- department must be string
- cgpa must be float

---

## Sample Data

```python
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
```

### Explanation

This list acts as a temporary database.

Important:

- Data exists only in memory.
- Restarting the server removes all changes.

---

## Home Endpoint

```python
@app.get("/")
def home():
    return {"message": "Student Management API Running"}
```

### Explanation

Purpose:

- Verifies API is running.
- Returns a welcome message.

Request:

```http
GET /
```

Response:

```json
{
  "message": "Student Management API Running"
}
```

---

## GET All Students

```python
@app.get("/students")
def get_all_students():
    return students
```

### Explanation

Returns every student.

Request:

```http
GET /students
```

Operation Type:

READ (CRUD)

---

## GET Student By ID

```python
@app.get("/student/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
```

### Explanation

Path Parameter Example:

```http
/student/2
```

student_id is extracted from URL.

Flow:

1. Loop through students.
2. Compare IDs.
3. Return matching student.
4. Return 404 if not found.

---

## Filter Students by Department

```python
@app.get("/students/filter")
def filter_students(department: str):

    result = [
        student
        for student in students
        if student["department"].lower() == department.lower()
    ]

    return result
```

### Explanation

Query Parameter Example:

```http
/students/filter?department=CSE
```

Used for:

- filtering
- searching
- sorting
- pagination

Returns students belonging to the given department.

---

## Create Student (POST)

```python
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
```

### Explanation

Purpose:

Create a new student.

Request:

```http
POST /student
```

Request Body:

```json
{
  "id": 4,
  "name": "Karthik",
  "department": "AI",
  "cgpa": 8.8
}
```

Process:

1. Validate request.
2. Check duplicate ID.
3. Add student.
4. Return success response.

CRUD Operation:

CREATE

---

## Update Student (PUT)

```python
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
```

### Explanation

Purpose:

Update existing student information.

Request:

```http
PUT /student/2
```

Flow:

1. Find student.
2. Replace old data.
3. Return updated record.
4. Return 404 if student does not exist.

CRUD Operation:

UPDATE

---

## Delete Student (DELETE)

```python
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
```

### Explanation

Purpose:

Remove a student.

Request:

```http
DELETE /student/3
```

Flow:

1. Find student.
2. Remove from list.
3. Return deleted record.

CRUD Operation:

DELETE

---

# CRUD Summary

## Create

```http
POST /student
```

Adds data.

## Read

```http
GET /students
GET /student/{id}
```

Fetches data.

## Update

```http
PUT /student/{id}
```

Updates data.

## Delete

```http
DELETE /student/{id}
```

Deletes data.

---
CRUD Summary
Operation	HTTP Method
Create	POST
Read	GET
Update	PUT
Delete	DELETE

# Run the Application

```bash
pip install fastapi uvicorn
```

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Practice Exercises

## Exercise 1

Add fields:

```python
age: int
email: str
```

## Exercise 2

Create endpoint:

```http
GET /students/count
```

Return total number of students.

## Exercise 3

Create endpoint:

```http
GET /students/topper
```

Return student with highest CGPA.

## Exercise 4

Create endpoint:

```http
GET /students/search?name=Rahul
```

Search a student using name.

## Exercise 5

Add validation:

```python
from pydantic import Field

cgpa: float = Field(..., ge=0, le=10)
age: int = Field(..., ge=16, le=40)
```

This ensures valid CGPA and age values.
