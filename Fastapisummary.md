# FastAPI for AI Engineers - Complete Learning Guide (Parts 1–7)

> A structured learning guide covering FastAPI fundamentals, CRUD operations, databases, validation, authentication, JWTs, and route protection.

---

# Table of Contents

1. Introduction to APIs and FastAPI
2. Understanding Modern AI Backends
3. FastAPI Architecture
4. Building Your First FastAPI Project
5. CRUD Operations
6. Path Parameters vs Query Parameters
7. Request Bodies and Pydantic
8. Database Integration with SQLite
9. SQLAlchemy ORM
10. Project Structure Best Practices
11. Data Validation with Pydantic
12. Authentication vs Authorization
13. Password Hashing
14. JWT Authentication
15. Protecting Routes
16. OAuth2PasswordBearer
17. Dependency Injection
18. Complete Backend Request Flow
19. FastAPI Learning Roadmap
20. Best Practices

---

# 1. Introduction to APIs

## What is an API?

API stands for:

**Application Programming Interface**

An API allows two software systems to communicate.

Example:

```text
Frontend
    ↓
Backend API
    ↓
Database
    ↓
Response
```

Response Example:

```json
{
    "message": "Hello World"
}
```

APIs are the backbone of modern applications.

Examples:

- Instagram
- Netflix
- Spotify
- Uber
- ChatGPT
- AI Agents
- RAG Applications

---

# 2. Understanding Modern AI Backends

Traditional Web Application:

```text
User
 ↓
Frontend
 ↓
Backend
 ↓
Database
```

Modern AI Application:

```text
User
 ↓
Frontend
 ↓
FastAPI Backend
 ↓
LLM
 ↓
Vector Database
 ↓
External APIs
 ↓
Response
```

Modern AI systems frequently perform:

- LLM calls
- Embedding generation
- Vector searches
- Tool calling
- Streaming responses
- Multi-service communication

This increased demand for:

- Speed
- Scalability
- Async processing
- Better developer productivity

---

# 3. Why FastAPI?

FastAPI became the preferred backend framework for AI applications because it provides:

## High Performance

Built on:

- Starlette
- ASGI
- Uvicorn

Performance is comparable to Node.js and Go for many API workloads.

---

## Async Support

FastAPI supports:

```python
async
await
```

Useful when waiting for:

- LLM responses
- Database calls
- API requests
- Cloud services

Example:

```python
@app.get("/chat")
async def chat():
    result = await llm_response()
    return result
```

---

## Automatic Validation

FastAPI uses Pydantic.

Example:

```python
class Student(BaseModel):
    name: str
    cgpa: float
```

Invalid data is automatically rejected.

---

## Automatic Documentation

FastAPI generates Swagger UI automatically.

```text
http://localhost:8000/docs
```

---

# 4. Creating Your First FastAPI Application

Install:

```bash
pip install fastapi uvicorn
```

Create:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
```

Run:

```bash
uvicorn main:app --reload
```

Visit:

```text
http://localhost:8000/docs
```

---

# 5. CRUD Operations

CRUD stands for:

| Operation | Description |
|------------|-------------|
| Create | Add data |
| Read | Retrieve data |
| Update | Modify data |
| Delete | Remove data |

Most backend systems are built around CRUD.

Examples:

- User Management
- Orders
- Students
- Products
- Chat Sessions

---

# 6. Path Parameters and Query Parameters

## Path Parameters

Used when you know the exact resource.

Example:

```text
/student/5
```

Implementation:

```python
@app.get("/student/{id}")
def get_student(id: int):
    ...
```

Examples:

```text
/users/1
/orders/20
/products/100
```

---

## Query Parameters

Used for filtering and searching.

Example:

```text
/students?department=CSE
```

Implementation:

```python
@app.get("/students")
def students(department: str):
    ...
```

Common Uses:

- Filtering
- Searching
- Pagination
- Sorting

---

## Differences

### Path Parameter

```text
/student/1
```

Meaning:

"I want student 1"

### Query Parameter

```text
/students?department=CSE
```

Meaning:

"Filter students belonging to CSE"

---

# 7. Request Bodies Using Pydantic

Incoming data should follow a defined structure.

Example:

```python
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    department: str
    cgpa: float
```

POST Endpoint:

```python
@app.post("/student")
def create_student(student: Student):
    return student
```

Valid Request:

```json
{
  "id": 1,
  "name": "Ananya",
  "department": "CSE",
  "cgpa": 8.9
}
```

---

# 8. Why Databases Are Needed

Bad approach:

```python
students = []
```

Problem:

```text
Server Restarts
      ↓
Memory Cleared
      ↓
Data Lost
```

Applications need persistent storage.

Examples:

- User Accounts
- Orders
- Chat History
- AI Memory
- Documents

---

# 9. SQLite Database

SQLite is a lightweight relational database.

Example:

```text
students.db
```

Advantages:

- No installation
- Single file database
- Lightweight
- Easy development setup

Install:

```bash
pip install sqlalchemy
```

---

# 10. Understanding SQLAlchemy ORM

Without ORM:

```sql
SELECT * FROM students;
```

With ORM:

```python
student = Student()
```

Mapping:

```text
Database Table → Python Class
Database Row   → Python Object
Database Column → Object Attribute
```

Benefits:

- Cleaner code
- Less SQL writing
- Easier maintenance

---

# 11. Recommended Project Structure

```text
project/
│
├── database.py
├── models.py
├── schemas.py
├── main.py
└── students.db
```

---

## database.py

Contains:

- Database connection
- Session management
- Base class

---

## models.py

Contains:

- Database tables

Example:

```python
class Student(Base):
    ...
```

---

## schemas.py

Contains:

- Validation schemas
- Request models
- Response models

---

## main.py

Contains:

- Routes
- Business logic

---

# 12. Data Validation with Pydantic

Validation protects your application from bad data.

Examples:

- Age cannot be negative
- Email must be valid
- CGPA between 0 and 10
- Temperature must be numeric

---

## Model Example

```python
class Student(BaseModel):
    name: str
    department: str
    cgpa: float
```

---

## Valid Request

```json
{
    "name": "Ananya",
    "department": "CSE",
    "cgpa": 8.9
}
```

---

## Invalid Request

```json
{
    "name": "Ananya",
    "department": "CSE",
    "cgpa": "Excellent"
}
```

FastAPI automatically returns validation errors.

---

# 13. Adding Constraints

Using `Field()`:

```python
from pydantic import Field

class Student(BaseModel):
    name: str = Field(min_length=3)
    cgpa: float = Field(ge=0, le=10)
```

Rules:

- Minimum length
- Maximum length
- Minimum value
- Maximum value

---

# 14. Authentication vs Authorization

Many beginners confuse these concepts.

---

## Authentication

Authentication answers:

```text
Who are you?
```

Examples:

- Username
- Password
- JWT Token

Example:

```text
Login
 ↓
Verify Identity
 ↓
Authenticated
```

---

## Authorization

Authorization answers:

```text
What can you do?
```

Examples:

- Admin access
- Premium user access
- Delete permissions

Example:

```text
Authenticated
 ↓
Check Role
 ↓
Allowed / Denied
```

---

## Comparison

### Authentication

- Verifies identity
- Happens first

### Authorization

- Verifies permissions
- Happens after authentication

---

# 15. Password Hashing

Never store passwords like:

```python
users = {
    "rahul": "password123"
}
```

This is dangerous.

Instead use hashing.

Install:

```bash
pip install passlib[bcrypt]
```

Create Hasher:

```python
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
```

---

## Hash Password

```python
hashed_password = pwd_context.hash("password123")
```

Output:

```text
$2b$12$...
```

---

## Verify Password

```python
pwd_context.verify(
    "password123",
    hashed_password
)
```

Returns:

```python
True
```

---

# 16. JWT Authentication

JWT means:

**JSON Web Token**

Instead of sending username/password every time:

```text
User
 ↓
Login
 ↓
Receive JWT
 ↓
Use JWT for future requests
```

---

## Install JWT Library

```bash
pip install python-jose
```

---

## JWT Configuration

```python
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
```

Secret key signs tokens.

If token is modified:

```text
Signature Verification Fails
```

---

## Create Token

```python
from jose import jwt

def create_access_token(data: dict):
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
```

Example Payload:

```json
{
    "sub": "suman"
}
```

---

# 17. Route Protection

Creating a JWT is not enough.

Endpoints must verify tokens.

---

## Unprotected Route

```python
@app.get("/profile")
def profile():
    return {
        "message": "My Profile"
    }
```

Anyone can access it.

---

# 18. OAuth2PasswordBearer

FastAPI provides:

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
```

Incoming Request:

```http
Authorization: Bearer eyJh...
```

FastAPI extracts the token automatically.

---

# 19. Verifying JWT Tokens

Example:

```python
from jose import jwt

def verify_token(token):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload.get("sub")
```

Extracts:

```json
{
    "sub": "suman"
}
```

---

# 20. Dependency Injection with Depends

FastAPI uses:

```python
Depends()
```

to inject dependencies.

Example:

```python
from fastapi import Depends
```

Current User Dependency:

```python
def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    ...
```

Responsibilities:

1. Extract token
2. Verify token
3. Identify user
4. Return user

---

# 21. Protected Routes

```python
@app.get("/profile")
def profile(
    current_user = Depends(
        get_current_user
    )
):
    return {
        "message":
        f"Welcome {current_user}"
    }
```

---

## Valid Token

```json
{
    "message": "Welcome suman"
}
```

---

## Invalid Token

```json
{
    "detail": "Could not validate credentials"
}
```

---

# 22. Complete FastAPI Authentication Flow

```text
User Registers
        ↓
Password Hashed
        ↓
Stored in Database
        ↓
User Login
        ↓
Verify Password
        ↓
Generate JWT
        ↓
JWT Returned
        ↓
Client Stores Token
        ↓
User Requests Protected Route
        ↓
Bearer Token Sent
        ↓
FastAPI Extracts Token
        ↓
Verify JWT
        ↓
Identify User
        ↓
Grant Access
```

---

# 23. AI Backend Architecture Using FastAPI

```text
Frontend
    ↓
FastAPI
    ↓
Authentication
    ↓
Business Logic
    ↓
LLM
    ↓
Embeddings
    ↓
Vector Database
    ↓
SQL Database
    ↓
Response
```

FastAPI sits at the center of modern AI applications.

---

# 24. Recommended Learning Path

### Foundation

✅ APIs

✅ HTTP Methods

✅ JSON

✅ FastAPI Basics

---

### Core Backend

✅ CRUD

✅ Path Parameters

✅ Query Parameters

✅ Request Bodies

---

### Data Layer

✅ SQLite

✅ SQLAlchemy

✅ ORM Concepts

---

### Validation

✅ Pydantic

✅ Field Constraints

✅ Schema Design

---

### Security

✅ Authentication

✅ Authorization

✅ Password Hashing

✅ JWT

✅ Route Protection

---

# 25. Final Takeaways

By completing Parts 1–7, you should understand:

- How APIs work
- Why FastAPI is popular for AI applications
- CRUD operations
- Path and query parameters
- Pydantic validation
- Database integration using SQLite
- SQLAlchemy ORM
- Authentication vs Authorization
- Password hashing with bcrypt
- JWT token generation
- JWT verification
- OAuth2PasswordBearer
- Dependency Injection
- Protected Routes

These concepts form the foundation required to build production-ready FastAPI backends for AI applications, SaaS platforms, chatbots, RAG systems, and agentic workflows.
