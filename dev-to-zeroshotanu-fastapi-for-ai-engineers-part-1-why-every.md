You open ChatGPT.

You type a prompt.

Within seconds:

- your request reaches a backend server,
- the backend communicates with an LLM,
- retrieves memory,
- queries vector databases,
- processes context,
- and streams responses back to you in real time.

Modern AI applications are no longer just “apps.”

They are systems made up of multiple services constantly communicating with each other through APIs.

And one framework has quietly become the default choice for building these modern AI backends:

**FastAPI.**

In this article, we’ll understand:

- why APIs are essential,
- why modern AI systems depend heavily on them,
- what FastAPI actually is,
- and why it became the preferred backend framework for AI engineers.

* * *

## Modern Applications Are API Systems

Most applications today are distributed systems.

Your frontend, backend, database, authentication service, payment gateway, and AI models continuously exchange data with one another.

When you order food online:

```
Frontend → Backend API → Database → Response
```

Enter fullscreen modeExit fullscreen mode

When you use an AI chatbot:

```
User → FastAPI Backend → LLM → Vector DB → Response
```

Enter fullscreen modeExit fullscreen mode

Without APIs:

- frontend applications would directly access databases,
- systems would become tightly coupled,
- security would become difficult,
- scaling would become messy,
- and AI applications would be extremely difficult to maintain.

APIs act as communication bridges between systems.

They define:

- how requests are sent,
- what data is expected,
- and what responses should be returned.

Modern software runs on APIs.

Modern AI systems depend on them even more.

* * *

## What Exactly Is an API?

API stands for **Application Programming Interface**.

In simple terms:

> An API allows two software systems to communicate with each other.

For example:

- a frontend sends a request,
- the backend processes it,
- and returns a response (usually JSON).

Example:

```
{
    "message": "Hello World"
}
```

Enter fullscreen modeExit fullscreen mode

Every major application you use today relies heavily on APIs:

- Instagram
- Netflix
- Uber
- Spotify
- ChatGPT
- AI agents
- recommendation systems
- RAG applications

APIs are the foundation of modern backend engineering.

* * *

## Why AI Applications Changed Backend Development

Traditional web applications were already API-heavy.

But AI applications introduced entirely new backend challenges.

Modern AI systems constantly:

- communicate with LLM APIs,
- query vector databases,
- retrieve embeddings,
- stream responses,
- interact with external tools,
- and handle concurrent requests.

This created a need for backend frameworks that were:

- lightweight,
- fast,
- asynchronous,
- scalable,
- and developer-friendly.

That’s where FastAPI entered.

* * *

## What Is FastAPI?

FastAPI is a modern Python framework designed specifically for building APIs.

It became popular because it combines:

- high performance,
- async support,
- automatic validation,
- clean developer experience,
- and excellent scalability.

FastAPI is built on top of:

- **Starlette** → provides ASGI and async capabilities
- **Pydantic** → handles data validation
- **Uvicorn** → runs FastAPI applications efficiently

Together, this stack became perfect for modern AI systems.

```

        Client Request
               │
               ▼
         ┌─────────┐
         │ FastAPI │
         └────┬────┘
              │
     ┌────────┼────────┐
     ▼                 ▼
 Starlette         Pydantic
 (ASGI/Async)     (Validation)
              │
              ▼
           Uvicorn
        (ASGI Server)
```

Enter fullscreen modeExit fullscreen mode

* * *

## Why FastAPI Became the Standard for AI Backends

## 1\. Async Support

This is one of the biggest reasons FastAPI exploded in popularity.

AI applications constantly wait for:

- LLM responses,
- vector database retrieval,
- external APIs,
- embeddings,
- cloud services.

FastAPI supports asynchronous programming using Python’s `async` and `await`.

Example:

```
async def generate_response():
    return {"message": "Async response"}
```

Enter fullscreen modeExit fullscreen mode

Instead of blocking the server while waiting for responses, FastAPI can efficiently handle multiple requests concurrently.

For AI systems, this matters a lot.

* * *

## 2\. Built on Starlette

FastAPI uses Starlette underneath.

Starlette provides:

- ASGI support,
- middleware,
- WebSockets,
- background tasks,
- async request handling.

This makes FastAPI much better suited for modern real-time AI applications compared to older synchronous architectures.

* * *

## 3\. Powered by Uvicorn

FastAPI applications are commonly run using Uvicorn.

Start a FastAPI server using:

```
uvicorn main:app --reload
```

Enter fullscreen modeExit fullscreen mode

Here:

- `main` → filename
- `app` → FastAPI instance
- `--reload` → automatically reloads during development

Uvicorn is an ASGI server optimized for high-performance asynchronous applications.

* * *

## 4\. Automatic Swagger UI Documentation

One of FastAPI’s most loved features is automatic API documentation.

The moment you create routes, FastAPI automatically generates interactive API documentation for you.

Visit:

```
http://127.0.0.1:8000/docs
```

Enter fullscreen modeExit fullscreen mode

You can:

- test endpoints,
- send requests,
- inspect responses,
- and debug APIs directly from the browser.

This becomes incredibly useful when:

- working with frontend developers,
- building AI APIs,
- or testing backend systems quickly.

* * *

## 5\. Automatic Data Validation Using Pydantic

FastAPI uses Python type hints for validation.

Example:

```
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Enter fullscreen modeExit fullscreen mode

If invalid data is sent, FastAPI automatically validates and rejects it.

This removes a huge amount of manual validation code developers previously had to write themselves.

* * *

## Installing FastAPI

Install FastAPI and Uvicorn:

```
pip install fastapi uvicorn
```

Enter fullscreen modeExit fullscreen mode

* * *

## Your First FastAPI Application

Create a file called `main.py`

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Dev.io"}
```

Enter fullscreen modeExit fullscreen mode

![Sample example of home function](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffroaj5gsyore8nbdjufr.png)

Run the server:

```
uvicorn main:app --reload
```

Enter fullscreen modeExit fullscreen mode

Open:

```
http://127.0.0.1:8000/docs
```

Enter fullscreen modeExit fullscreen mode

![Sample example of Swagger UI docs](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fo6rrj2igftkg7gpiim6k.png)

And you’ll see FastAPI’s automatically generated Swagger UI.

At this point, you already have:

- a running backend server,
- a working API,
- and interactive API documentation.

With surprisingly little code.

* * *

## Why FastAPI Matters for AI Engineers

FastAPI became extremely popular because modern AI applications are fundamentally API systems.

It is heavily used for:

- RAG pipelines,
- AI agents,
- chatbot backends,
- LangChain applications,
- vector database APIs,
- recommendation systems,
- and model-serving APIs.

Modern AI engineering is not just about building models anymore.

It’s also about building scalable systems around those models.

And FastAPI fits perfectly into that ecosystem.

* * *

## Final Thoughts

FastAPI didn’t become popular accidentally.

It became the framework of choice for AI engineers because modern AI systems are:

- asynchronous,
- API-driven,
- performance-sensitive,
- and highly modular.

Whether you're building:

- AI agents,
- chat systems,
- RAG applications,
- or production AI platforms,

FastAPI provides the exact architecture modern AI applications need.

* * *

## What’s Next?

Right now, our API returns data, but it doesn’t actually store anything permanently.

In the next article, we’ll build real CRUD APIs using FastAPI and understand:

- GET requests,
- POST requests,
- PUT requests,
- DELETE requests,
- and how backend applications manage data.

Then we’ll move toward integrating databases like SQLite and MySQL in the following parts of this series.


In the previous article, we explored why FastAPI has become one of the most popular backend frameworks for modern AI applications.

If you haven't read the previous post, check it out: [https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-1-why-every-ai-backend-is-moving-toward-fastapi-45fg](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-1-why-every-ai-backend-is-moving-toward-fastapi-45fg)

Now it's time to build something practical.

Most backend applications revolve around four basic operations:

- Create
- Read
- Update
- Delete

Together, these operations are known as **CRUD**.

Whether you're building:

- a social media application,
- an e-commerce platform,
- a chatbot,
- or an AI agent,

CRUD operations are the foundation of backend development.

In this article, we'll build a simple Student Management API while learning:

- Path Parameters
- Query Parameters
- GET Requests
- POST Requests
- PUT Requests
- DELETE Requests

* * *

## Creating Sample Data

Let's start with a small dataset.

```
from fastapi import FastAPI

app = FastAPI()

students = [\
    {\
        "id": 1,\
        "name": "Ananya",\
        "department": "CSE",\
        "cgpa": 8.9\
    },\
    {\
        "id": 2,\
        "name": "Rahul",\
        "department": "ECE",\
        "cgpa": 8.4\
    },\
    {\
        "id": 3,\
        "name": "Priya",\
        "department": "IT",\
        "cgpa": 9.1\
    }\
]
```

Enter fullscreen modeExit fullscreen mode

Run the application:

```
uvicorn main:app --reload
```

Enter fullscreen modeExit fullscreen mode

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

Enter fullscreen modeExit fullscreen mode

* * *

## Path Parameters

A path parameter is part of the URL itself.

```
/student/2
```

Enter fullscreen modeExit fullscreen mode

Here, `2` is the path parameter.

Think of path parameters as:

"I know exactly which resource I want."

Examples:

```
/users/10
/products/25
/orders/1001
/student/2
```

Enter fullscreen modeExit fullscreen mode

Let's fetch a specific student using their ID.

```
@app.get("/student/{id}")
def get_student_info(id: int):

    for user in students:
        if user["id"] == id:
            return user

    return {"message": "Student not found"}
```

Enter fullscreen modeExit fullscreen mode

Request:

```
/student/2
```

Enter fullscreen modeExit fullscreen mode

Response:

```
{
    "id": 2,
    "name": "Rahul",
    "department": "ECE",
    "cgpa": 8.4
}
```

Enter fullscreen modeExit fullscreen mode

* * *

## Query Parameters

A query parameter appears after the `?` in a URL.

```
/student?department="CSE"
```

Enter fullscreen modeExit fullscreen mode

They are commonly used for:

- filtering
- searching
- sorting
- pagination

Let's implement the same endpoint using a query parameter.

```
@app.get("/students")
def get_students(department: str):

    filtered_students = []

    for student in students:
        if student["department"] == department:
            filtered_students.append(student)

    return filtered_students
```

Enter fullscreen modeExit fullscreen mode

Request:

```
/student?department="CSE"
```

Enter fullscreen modeExit fullscreen mode

Response:

```
{
    "id": 1,
    "name": "Ananya",
    "department": "CSE",
    "cgpa": 8.9
}
```

Enter fullscreen modeExit fullscreen mode

All students in CSE department would be filtered.

Query parameters are often optional and are used to modify, filter, or search results.

### Path vs Query Parameters

| Path Parameter | Query Parameter |
| --- | --- |
| Part of URL path | Appears after ? |
| Identifies a resource | Filters or searches |
| `/student/1` | `/student?id=1` |

* * *

## GET Request

GET requests are used to retrieve data.

```
@app.get("/students")
def get_all_students():
    return students
```

Enter fullscreen modeExit fullscreen mode

Response:

```
[\
    {\
        "id": 1,\
        "name": "Ananya",\
        "department": "CSE",\
        "cgpa": 8.9\
    },\
    {\
        "id": 2,\
        "name": "Rahul",\
        "department": "ECE",\
        "cgpa": 8.4\
    },\
    {\
        "id": 3,\
        "name": "Priya",\
        "department": "IT",\
        "cgpa": 9.1\
    }\
]
```

Enter fullscreen modeExit fullscreen mode

* * *

## Request Bodies with Pydantic

When users send data to our API, FastAPI needs a way to validate that the incoming data has the correct structure.

This is where Pydantic comes in.

Pydantic allows us to define the expected shape of incoming data using Python classes.

For example, every student should have:

- an ID
- a name
- a department
- a CGPA

We can define this structure using a Pydantic model.

```
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    department: str
    cgpa: float
```

Enter fullscreen modeExit fullscreen mode

Now FastAPI automatically validates incoming requests.

For example, this request is valid:

{

"id": 4,

"name": "Karthik",

"department": "AI",

"cgpa": 8.8

}

But if someone sends:

{

"id": "four",

"name": "Karthik"

}

FastAPI will automatically return a validation error because:

id should be an integer

required fields are missing

This saves us from writing validation code manually.

We'll explore Pydantic, validation, optional fields, custom validators, and advanced request handling in a dedicated article later in this series.

## POST Request

POST requests are used to create new resources.

```
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    department: str
    cgpa: float
```

Enter fullscreen modeExit fullscreen mode

```
@app.post("/student")
def add_student(student: Student):

    students.append(student.dict())

    return {
        "message": "Student added successfully",
        "student": student
    }
```

Enter fullscreen modeExit fullscreen mode

Request Body:

```
{
    "id": 4,
    "name": "Karthik",
    "department": "AI",
    "cgpa": 8.8
}
```

Enter fullscreen modeExit fullscreen mode

* * *

## PUT Request

PUT requests are used to update existing resources.

```
@app.put("/student/{id}")
def update_student(id: int, updated_student: Student):

    for index, user in enumerate(students):

        if user["id"] == id:

            students[index] = updated_student.dict()

            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    return {"message": "Student not found"}
```

Enter fullscreen modeExit fullscreen mode

Request:

```
PUT /student/2
```

Enter fullscreen modeExit fullscreen mode

* * *

## DELETE Request

DELETE requests are used to remove resources.

```
@app.delete("/student/{id}")
def delete_student(id: int):

    for index, user in enumerate(students):

        if user["id"] == id:

            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    return {"message": "Student not found"}
```

Enter fullscreen modeExit fullscreen mode

Request:

```
DELETE /student/3
```

Enter fullscreen modeExit fullscreen mode

* * *

## CRUD Summary

| Operation | HTTP Method |
| --- | --- |
| Create | POST |
| Read | GET |
| Update | PUT |
| Delete | DELETE |

CRUD operations form the foundation of almost every backend application you'll build.

* * *

In the previous article, we explored how to build our first CRUD API using FastAPI. While our API worked correctly, there was one major problem.

We were storing data inside Python lists, which exist only in memory.

If you've ever wondered how applications like Instagram, LinkedIn, or ChatGPT remember information even after a server restart, the answer is simple: databases.

In this article, we'll solve the problem of in-memory storage by connecting our FastAPI application to SQLite using SQLAlchemy.

If you haven't read the previous post, check it out:

[FastAPI for AI Engineers - Part 2: Building Your First CRUD API](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-2-building-your-first-crud-api-lpl)

[![zeroshotanu profile](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3559285%2Fc3ef331f-5380-4103-9520-7e34720fd7dc.jpeg)](https://dev.to/zeroshotanu)

[Ananya S](https://dev.to/zeroshotanu)

Ananya S



[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3559285%2Fc3ef331f-5380-4103-9520-7e34720fd7dc.jpeg)Ananya S](https://dev.to/zeroshotanu)

Follow

[Jun 1](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-2-building-your-first-crud-api-lpl)

## [FastAPI for AI Engineers - Part 2: Building Your First CRUD API](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-2-building-your-first-crud-api-lpl)

[#ai](https://dev.to/t/ai) [#backend](https://dev.to/t/backend) [#fastapi](https://dev.to/t/fastapi) [#python](https://dev.to/t/python)

[![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)7 reactions](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-2-building-your-first-crud-api-lpl) [CommentsAdd Comment](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-2-building-your-first-crud-api-lpl#comments)

4 min read


By the end of this article, you'll understand:

- Why in-memory storage is a problem
- What SQLite is
- What SQLAlchemy is
- How ORM works
- How to create database tables using Python classes
- How to perform CRUD operations using a real database

* * *

## The Problem with In-Memory Storage

Previously, our application stored students inside a Python list.

```
students = [\
    {\
        "id": 1,\
        "name": "Ananya",\
        "department": "CSE",\
        "cgpa": 8.9\
    }\
]
```

Enter fullscreen modeExit fullscreen mode

This worked for learning CRUD operations.

However, consider what happens when the server restarts:

```
FastAPI Server Stops
        ↓
Python Memory Cleared
        ↓
All Student Data Lost
```

Enter fullscreen modeExit fullscreen mode

This is unacceptable in real-world applications.

We need a place where data can survive application restarts.

This is where databases come in.

* * *

## What is SQLite?

SQLite is a lightweight relational database.

Unlike MySQL or PostgreSQL, SQLite doesn't require a separate database server.

Instead, everything is stored inside a single file.

```
students.db
```

Enter fullscreen modeExit fullscreen mode

Advantages of SQLite:

- No installation required
- Lightweight
- Easy to learn
- Perfect for local development
- Great for small projects

For this article, we'll use SQLite.

* * *

## What is SQLAlchemy?

Before SQLAlchemy, developers often wrote raw SQL queries.

Example:

```
SELECT * FROM students;
```

Enter fullscreen modeExit fullscreen mode

While SQL is powerful, writing queries everywhere quickly becomes difficult to maintain.

SQLAlchemy solves this problem using an ORM.

* * *

## What is an ORM?

ORM stands for Object Relational Mapper.

It allows us to interact with database tables using Python classes.

Think of it like a translator.

| Database | Python |
| --- | --- |
| Table | Class |
| Row | Object |
| Column | Attribute |

For example:

Database table:

```
students

id     name     department     cgpa
1      Ananya   CSE            8.9
```

Enter fullscreen modeExit fullscreen mode

becomes:

```
class Student(Base):
    ...
```

Enter fullscreen modeExit fullscreen mode

Instead of writing SQL manually, we work with Python objects.

SQLAlchemy generates SQL behind the scenes.

* * *

## Project Structure

Create the following structure:

```
project/
│
├── database.py
├── models.py
├── schemas.py
├── main.py
└── students.db
```

Enter fullscreen modeExit fullscreen mode

Each file has a specific responsibility.

### database.py

Responsible for:

- Database connection
- Session creation
- Base class creation

### models.py

Responsible for:

- Database tables

### schemas.py

Responsible for:

- Request validation
- Response structure

### main.py

Responsible for:

- API routes
- Business logic

* * *

## Installing Dependencies

```
pip install sqlalchemy
```

Enter fullscreen modeExit fullscreen mode

If you haven't installed FastAPI yet:

```
pip install fastapi uvicorn
```

Enter fullscreen modeExit fullscreen mode

* * *

## Step 1: Creating database.py

Create a file named `database.py`

```
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} #allows the same connection to be used across threads
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

Enter fullscreen modeExit fullscreen mode

Normally, SQLAlchemy uses transactional mode:

You make changes → they are staged in the session → you call commit() to persist them.

If autocommit is enabled, each statement is committed immediately (like SQLite’s default).

When autoflush=True (default), SQLAlchemy automatically flushes pending changes to the database before executing a query.

Flush means:

Synchronize in-memory changes with the database inside the current transaction.

Does not commit — changes are still rollback-able until you call commit().

* * *

## Understanding create\_engine()

```
engine = create_engine(...)
```

Enter fullscreen modeExit fullscreen mode

SQLAlchemy needs a way to communicate with the database.

The Engine object acts as the bridge between FastAPI and SQLite.

Whenever we:

- insert data
- retrieve data
- update data
- delete data

SQLAlchemy uses the engine to talk to the database.

* * *

## Understanding SessionLocal

```
SessionLocal = sessionmaker(...)
```

Enter fullscreen modeExit fullscreen mode

A session represents a conversation with the database.

Imagine visiting a bank:

1. Start conversation
2. Perform transactions
3. End conversation

A database session works similarly.

Every database operation happens through a session.

* * *

## Understanding Base

```
Base = declarative_base()
```

Enter fullscreen modeExit fullscreen mode

Every database model we create will inherit from Base.

SQLAlchemy uses Base to keep track of all models and create tables automatically.

* * *

## Creating Database Sessions

Add this function below the previous code.

```
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
```

Enter fullscreen modeExit fullscreen mode

* * *

## Why Do We Need get\_db()?

Without this function, every route would need to create and close sessions manually.

Example:

```
@app.get("/students")
def get_students():

    db = SessionLocal()

    # Database operations

    db.close()
```

Enter fullscreen modeExit fullscreen mode

This becomes repetitive.

Instead, FastAPI can automatically create and close sessions for us.

Later we'll use:

```
db: Session = Depends(get_db)
```

Enter fullscreen modeExit fullscreen mode

FastAPI will:

1. Create a session
2. Give it to the route
3. Close it automatically

This is called Dependency Injection.

* * *

## Step 2: Creating models.py

Create a file named `models.py`

```
from sqlalchemy import Column, Integer, String, Float

from database import Base

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    cgpa = Column(Float)
```

Enter fullscreen modeExit fullscreen mode

* * *

## Understanding the Model

```
__tablename__ = "students"
```

Enter fullscreen modeExit fullscreen mode

This creates a table named:

```
students
```

Enter fullscreen modeExit fullscreen mode

* * *

```
id = Column(Integer, primary_key=True)
```

Enter fullscreen modeExit fullscreen mode

Creates the primary key.

Every student must have a unique ID.

* * *

```
name = Column(String)
```

Enter fullscreen modeExit fullscreen mode

Creates a text column.

The same applies to department.

* * *

```
cgpa = Column(Float)
```

Enter fullscreen modeExit fullscreen mode

Creates a floating-point column.

* * *

## Step 3: Creating schemas.py

Create a file named `schemas.py`

```
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    department: str
    cgpa: float

class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True
```

Enter fullscreen modeExit fullscreen mode

* * *

## Why Do We Need Schemas?

Schemas define what data our API expects.

For now, think of schemas as blueprints.

We're using Pydantic behind the scenes.

We'll explore:

- Validation
- Optional fields
- Custom validators
- Response models

in a dedicated article later in this series.

* * *

## Step 4: Creating main.py

```
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas

from database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
```

Enter fullscreen modeExit fullscreen mode

* * *

## Creating Tables Automatically

```
models.Base.metadata.create_all(bind=engine)
```

Enter fullscreen modeExit fullscreen mode

When FastAPI starts:

1. SQLAlchemy checks all models.
2. Looks for missing tables.
3. Creates them automatically.

Our Student table is now created inside SQLite.

* * *

## CREATE Operation

```
@app.post("/student", response_model=schemas.StudentResponse)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = models.Student(
        name=student.name,
        department=student.department,
        cgpa=student.cgpa
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student
```

Enter fullscreen modeExit fullscreen mode

### What Happens Here?

```
db.add(new_student)
```

Enter fullscreen modeExit fullscreen mode

Adds the object to the session.

* * *

```
db.commit()
```

Enter fullscreen modeExit fullscreen mode

Permanently saves data to the database.

* * *

```
db.refresh(new_student)
```

Enter fullscreen modeExit fullscreen mode

Reloads the object from the database.

This is useful because the database automatically generates the ID.

* * *

## READ Operation

Get all students.

```
@app.get("/students")
def get_students(
    db: Session = Depends(get_db)
):

    return db.query(models.Student).all()
```

Enter fullscreen modeExit fullscreen mode

* * *

Get a student by ID.

```
@app.get("/student/{id}")
def get_student(
    id: int,
    db: Session = Depends(get_db)
):

    return (
        db.query(models.Student)
        .filter(models.Student.id == id)
        .first()
    )
```

Enter fullscreen modeExit fullscreen mode

* * *

## UPDATE Operation

```
@app.put("/student/{id}")
def update_student(
    id: int,
    updated_student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    student = (
        db.query(models.Student)
        .filter(models.Student.id == id)
        .first()
    )

    if not student:
        return {"message": "Student not found"}

    student.name = updated_student.name
    student.department = updated_student.department
    student.cgpa = updated_student.cgpa

    db.commit()

    db.refresh(student)

    return student
```

Enter fullscreen modeExit fullscreen mode

* * *

## DELETE Operation

```
@app.delete("/student/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(models.Student)
        .filter(models.Student.id == id)
        .first()
    )

    if not student:
        return {"message": "Student not found"}

    db.delete(student)

    db.commit()

    return {"message": "Student deleted successfully"}
```

Enter fullscreen modeExit fullscreen mode

* * *

## Running the Application

Start the server:

```
uvicorn main:app --reload
```

Enter fullscreen modeExit fullscreen mode

Open:

```
http://127.0.0.1:8000/docs
```

Enter fullscreen modeExit fullscreen mode

Use Swagger UI to:

- Create students
- Retrieve students
- Update students
- Delete students

* * *

## SQLite vs MySQL

The good news is that SQLAlchemy makes switching databases extremely easy.

Current SQLite connection:

```
DATABASE_URL = "sqlite:///./students.db"
```

Enter fullscreen modeExit fullscreen mode

MySQL connection:

```
MYSQL_USER = "root"
DB_PASSWORD = "123456" # use your MySQL login password
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'fastapi_db'

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{DB_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
```

Enter fullscreen modeExit fullscreen mode

Install the MySQL driver:

```
pip install pymysql
```

Enter fullscreen modeExit fullscreen mode

Everything else remains almost identical. Ensure you have MySQL in your desktop, open MySQL WorkBench and connect to database to see the database and tables in it. Ensure the database with the name 'fastapi\_db' is already present in MySQL WorkBench.

This is one of the biggest advantages of using an ORM.

* * *

## How Everything Works Together

```
Client Request
      │
      ▼
FastAPI Route
      │
      ▼
Pydantic Schema
      │
      ▼
Database Session
      │
      ▼
SQLAlchemy Model
      │
      ▼
SQLite / MySQL
```

Enter fullscreen modeExit fullscreen mode

When a user creates a student:

1. FastAPI receives the request
2. Pydantic validates the incoming data
3. A database session is created
4. SQLAlchemy converts the Python object into SQL
5. SQLite stores the data permanently

* * *

## Conclusion

We've now moved beyond in-memory storage and built our first database-backed FastAPI application.

Most production AI applications use the same architecture, whether they're storing chat histories, user profiles, agent memory, evaluation results, or feedback data.

In the previous article, we connected our FastAPI application to a database using SQLite and SQLAlchemy.

We also used classes like:

```
class StudentCreate(BaseModel):
    name: str
    department: str
    cgpa: float
```

Enter fullscreen modeExit fullscreen mode

without fully understanding what was happening behind the scenes.

Today, we'll fix that.

### If you haven't read it check it out:     [FastAPI for AI Engineers - Part 3: Connecting to a database](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-3-connecting-to-a-database-30ca)        [![zeroshotanu profile](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3559285%2Fc3ef331f-5380-4103-9520-7e34720fd7dc.jpeg)](https://dev.to/zeroshotanu)      [Ananya S](https://dev.to/zeroshotanu)   Ananya S          [![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3559285%2Fc3ef331f-5380-4103-9520-7e34720fd7dc.jpeg)Ananya S](https://dev.to/zeroshotanu)    Follow              [Jun 6](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-3-connecting-to-a-database-30ca)          \#\# [FastAPI for AI Engineers - Part 3: Connecting to a database](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-3-connecting-to-a-database-30ca)    [\#ai](https://dev.to/t/ai) [\#fastapi](https://dev.to/t/fastapi) [\#python](https://dev.to/t/python) [\#backend](https://dev.to/t/backend)      [![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)7 reactions](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-3-connecting-to-a-database-30ca) [Comments\ \ 2 comments](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-3-connecting-to-a-database-30ca\#comments)     6 min read

* * *

## Why Do We Need Data Validation?

Imagine you're building a weather application.

A user asks:

> What is the temperature in Chennai?

A valid response might be:

```
35
```

Enter fullscreen modeExit fullscreen mode

or

```
35°C
```

Enter fullscreen modeExit fullscreen mode

But what if the API returns:

```
Sunny
```

Enter fullscreen modeExit fullscreen mode

This is clearly wrong.

Temperature should be represented as a number.

Even if the value itself is inaccurate, we still know that temperature must be numeric.

This is where validation becomes important.

Validation allows us to define rules about what data is acceptable before it enters our application.

For example:

- Temperature should be numeric
- Age cannot be negative
- CGPA should be between 0 and 10
- Email addresses should follow a valid format

Without validation, applications can receive invalid data and behave unexpectedly.

* * *

## The Problem Without Validation

Consider a student registration API.

```
@app.post("/student")
def create_student(student):
    return student
```

Enter fullscreen modeExit fullscreen mode

A user could send:

```
{
    "name": "Ananya",
    "cgpa": "Excellent"
}
```

Enter fullscreen modeExit fullscreen mode

The API would accept it.

But a CGPA should be a number, not text.

As applications grow, manually checking every field becomes difficult.

We need a better solution.

* * *

## Enter Pydantic

Pydantic is a Python library used for data validation.

FastAPI uses Pydantic extensively behind the scenes.

Instead of manually validating data, we define a schema.

```
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    cgpa: float
```

Enter fullscreen modeExit fullscreen mode

Now FastAPI knows:

- `name` must be a string
- `cgpa` must be a floating-point number

Whenever data arrives, FastAPI automatically validates it.

* * *

## Your First Pydantic Model

```
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    department: str
    cgpa: float
```

Enter fullscreen modeExit fullscreen mode

Think of this model as a blueprint.

Any incoming request must follow this structure.

### Valid Request

```
{
    "name": "Ananya",
    "department": "CSE",
    "cgpa": 8.9
}
```

Enter fullscreen modeExit fullscreen mode

### Invalid Request

```
{
    "name": "Ananya",
    "department": "CSE",
    "cgpa": "Excellent"
}
```

Enter fullscreen modeExit fullscreen mode

FastAPI will reject the request automatically.

* * *

## Using Pydantic with FastAPI

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    department: str
    cgpa: float

@app.post("/student")
def create_student(student: Student):
    return student
```

Enter fullscreen modeExit fullscreen mode

Notice this line:

```
student: Student
```

Enter fullscreen modeExit fullscreen mode

FastAPI now expects the incoming request body to match the `Student` schema.

* * *

## Understanding Validation Errors

Suppose we send:

```
{
    "name": "Ananya",
    "department": "CSE",
    "cgpa": "Excellent"
}
```

Enter fullscreen modeExit fullscreen mode

FastAPI returns a validation error before the request reaches our route.

You'll see an error similar to:

```
{
    "detail": [\
        {\
            "type": "float_parsing",\
            "msg": "Input should be a valid number"\
        }\
    ]
}
```

Enter fullscreen modeExit fullscreen mode

Instead of failing silently, FastAPI clearly tells us what went wrong.

* * *

## Adding Constraints with Field()

Validating types is useful.

But sometimes we need stricter rules.

For example:

- CGPA should be between 0 and 10
- Name should have a minimum length
- Age should always be positive

Pydantic provides `Field()` for this purpose.

```
from pydantic import BaseModel, Field

class Student(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=50
    )

    cgpa: float = Field(
        gt=0,
        lt=10
    )
```

Enter fullscreen modeExit fullscreen mode

* * *

## Understanding the Constraints

```
cgpa: float = Field(gt=0, lt=10)
```

Enter fullscreen modeExit fullscreen mode

This means:

```
CGPA > 0
CGPA < 10
```

Enter fullscreen modeExit fullscreen mode

### Valid Request

```
{
    "name": "Ananya",
    "cgpa": 8.9
}
```

Enter fullscreen modeExit fullscreen mode

### Invalid Request

```
{
    "name": "Ananya",
    "cgpa": 15
}
```

Enter fullscreen modeExit fullscreen mode

FastAPI immediately rejects the request.

* * *

## Optional Fields

Sometimes fields are not mandatory.

For example, a student may not have a department assigned yet.

```
from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):

    name: str
    department: Optional[str] = None
```

Enter fullscreen modeExit fullscreen mode

Now the department field becomes optional.

### Valid Request

```
{
    "name": "Ananya"
}
```

Enter fullscreen modeExit fullscreen mode

### Also Valid

```
{
    "name": "Ananya",
    "department": "CSE"
}
```

Enter fullscreen modeExit fullscreen mode

* * *

## Request Models vs Database Models

One question many beginners ask is:

> Why do we need both `schemas.py` and `models.py`?

Let's understand the difference.

### SQLAlchemy Model

```
class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cgpa = Column(Float)
```

Enter fullscreen modeExit fullscreen mode

This defines how data is stored in the database.

* * *

### Pydantic Model

```
class StudentCreate(BaseModel):
    name: str
    cgpa: float
```

Enter fullscreen modeExit fullscreen mode

This defines how data enters our API.

* * *

Think of it this way:

```
Database Structure
        ≠
API Structure
```

Enter fullscreen modeExit fullscreen mode

They may look similar, but they serve different purposes.

* * *

## Response Models

Pydantic can also control what data is returned from an API.

```
class StudentResponse(BaseModel):
    id: int
    name: str
    cgpa: float
```

Enter fullscreen modeExit fullscreen mode

```
@app.get(
    "/student/{id}",
    response_model=StudentResponse
)
def get_student(id: int):
    ...
```

Enter fullscreen modeExit fullscreen mode

This ensures the response always follows a consistent structure.

* * *

## Why Pydantic Matters for AI Applications

Suppose you're building an LLM API.

Expected request:

```
{
    "prompt": "Explain FastAPI",
    "temperature": 0.7,
    "max_tokens": 500
}
```

Enter fullscreen modeExit fullscreen mode

Without validation, a user could send:

```
{
    "prompt": "Explain FastAPI",
    "temperature": "very creative",
    "max_tokens": "a lot"
}
```

Enter fullscreen modeExit fullscreen mode

and your application would have to deal with invalid data.

Pydantic prevents invalid requests from ever reaching your business logic.

This becomes especially important when building:

- AI chatbots
- RAG applications
- Agentic systems
- Model inference APIs
- Multi-agent workflows

* * *

## How Validation Fits into the Request Lifecycle

```
Client Request
      │
      ▼
Pydantic Validation
      │
      ▼
FastAPI Route
      │
      ▼
Business Logic
      │
      ▼
Database / LLM
```

Enter fullscreen modeExit fullscreen mode

Pydantic acts as the first line of defense.

Only valid data reaches the rest of the application.

* * *

## Conclusion

Pydantic is one of the reasons FastAPI has become so popular. It allows us to build APIs that are safer, more predictable, and easier to maintain.

In the next article, we'll move into Authentication and Authorization and learn how to protect our APIs from unauthorized access.


In the previous article, we explored how Pydantic validates data before it enters our application.

For example, if an API expects a temperature value, sending text such as "Sunny" instead of a numeric value should be rejected.

Just as applications validate data before processing it, they must also validate users before granting access.

Not everyone should be able to access every endpoint or perform every action.

This brings us to two important concepts in backend development:

- Authentication
- Authorization

Although these terms are often used together, they solve different problems.

If you haven't read it already, check out the previous post to maintain continuity in the series and improve your understanding on FastAPI:

[FastAPI for AI Engineers - Part 4: Stop Bad Data Before It Breaks Your API (Pydantic and Data Validation)](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-4-stop-bad-data-before-it-breaks-your-api-pydantic-and-data-1l35)

[![zeroshotanu profile](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3559285%2Fc3ef331f-5380-4103-9520-7e34720fd7dc.jpeg)](https://dev.to/zeroshotanu)

[Ananya S](https://dev.to/zeroshotanu)

Ananya S



[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3559285%2Fc3ef331f-5380-4103-9520-7e34720fd7dc.jpeg)Ananya S](https://dev.to/zeroshotanu)

Follow

[Jun 9](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-4-stop-bad-data-before-it-breaks-your-api-pydantic-and-data-1l35)

## [FastAPI for AI Engineers - Part 4: Stop Bad Data Before It Breaks Your API (Pydantic and Data Validation)](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-4-stop-bad-data-before-it-breaks-your-api-pydantic-and-data-1l35)

[#ai](https://dev.to/t/ai) [#fastapi](https://dev.to/t/fastapi) [#backend](https://dev.to/t/backend) [#python](https://dev.to/t/python)

[![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)7 reactions](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-4-stop-bad-data-before-it-breaks-your-api-pydantic-and-data-1l35) [Comments\\
\\
4 comments](https://dev.to/zeroshotanu/fastapi-for-ai-engineers-part-4-stop-bad-data-before-it-breaks-your-api-pydantic-and-data-1l35#comments)

4 min read


Imagine entering an airport.

At the entrance, security checks your passport or government-issued ID to verify who you are.

This process is Authentication.

Once inside, not everyone can access every area.

Passengers can access waiting lounges, restaurants, and boarding gates.

Pilots, security personnel, and airport staff can access restricted areas that ordinary passengers cannot.

This process is Authorization.

The difference becomes clearer when we compare them side by side:

| Authentication | Authorization |
| --- | --- |
| Verifies identity | Determines permissions |
| Answers "Who are you?" | Answers "What can you do?" |
| Happens first | Happens after authentication |
| Login credentials, tokens | Roles and permissions |
| Example: Logging into an app | Example: Accessing the admin dashboard |

The following endpoint can be accessed by anyone:

```
from fastapi import FastAPI
app = FastAPI()

@app.get('/profile/')
def get_profile():
    return {'message': 'Your profile is here'}
```

Enter fullscreen modeExit fullscreen mode

There is no mechanism to verify who is making the request.

Whether the user is logged in or not, the endpoint remains accessible.

Authentication is the process of verifying a user's identity.

A typical authentication flow looks like this:

```
Login
  ↓
Username + Password
  ↓
Verify User
  ↓
Generate Token
  ↓
Access Protected Routes
```

Enter fullscreen modeExit fullscreen mode

## Authentication

```

users = {
    "suman": "password123"
}

@app.post("/login")
def login(username: str, password: str):

    if users.get(username) == password:
        return {"message": "Login successful"}

    return {"message": "Invalid credentials"}
```

Enter fullscreen modeExit fullscreen mode

_This is a simplified example used only to demonstrate the concept._

**In real-world applications, passwords should never be stored in plain text and authentication is usually implemented using JWT tokens, OAuth, or other secure mechanisms.**

Authentication confirms the identity of a user.

However, simply knowing who a user is does not determine what they are allowed to do.

This is where Authorization comes into play.

## Authorization

```
users = {
    "suman": {
        "role": "admin"
    },
    "rahul": {
        "role": "student"
    }
}

@app.delete("/student/{id}")
def delete_student(id: int, current_user: dict):

    if current_user["role"] != "admin":
        return {"message": "Access denied"}

    return {"message": f"Student {id} deleted"}
```

Enter fullscreen modeExit fullscreen mode

### To summarize:

Authentication -> Who are you?

Authorization -> What are you allowed to do?

## Authentication and Authorization in AI Applications

Suppose you're building an AI-powered learning platform.

Authentication determines:

- Which user is sending the request
- Whether the user is logged in
- Whether the access token is valid

Authorization determines:

- Whether the user can access premium AI models
- Whether the user can upload training datasets
- Whether the user can view analytics dashboards
- Whether the user can manage other users

Even if two users are authenticated, they may not have the same permissions.

This is why authentication and authorization are both essential in production AI systems.

```
User Request
      │
      ▼
Authentication
(Who are you?)
      │
      ▼
Authorization
(What can you do?)
      │
      ▼
Protected Resource
```

Enter fullscreen modeExit fullscreen mode

## Final Thoughts

Authentication and Authorization are often mentioned together, but they solve different problems.

Authentication verifies identity.

Authorization determines permissions.

A user must first prove who they are before the system can decide what they are allowed to do.

In this article, we focused on understanding the concepts behind Authentication and Authorization.

JWT (JSON Web Tokens) is one of the most common approaches used to authenticate users in modern APIs.

In the next article, we'll move beyond theory and implement JWT-based Authentication in FastAPI step-by-step, allowing us to generate access tokens, protect routes, and identify users securely.




