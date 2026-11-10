# Student Management REST API

A RESTful API built using **Python, FastAPI, MySQL, and SQLAlchemy** to manage student records through standard CRUD operations.

This project is being developed incrementally to understand backend development, REST architecture, database integration, and ORM-based database operations.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API framework |
| Pydantic | Data validation and serialization |
| MySQL | Relational database |
| SQLAlchemy | Object Relational Mapper (ORM) |
| PyMySQL | MySQL database driver |
| Uvicorn | ASGI server |

## Features

- RESTful API architecture
- CRUD operations for student records
- Request validation using Pydantic
- MySQL database integration
- SQLAlchemy ORM models
- Automatic API documentation through Swagger UI
- Database connection management

## Student Data Model

Each student record contains:

| Field | Type | Description |
|---|---|---|
| id | Integer | Auto-generated primary key |
| name | String | Student's name |
| age | Integer | Student's age |
| grade | String | Student's grade |

## Project Structure

```text
student-api/
│
├── database/
│   ├── __init__.py
│   └── connection.py
│
├── models/
│   ├── __init__.py
│   └── student.py
│
├── schemas/
│   ├── __init__.py
│   └── student.py
│
├── main.py
├── create_tables.py
├── test_connection.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a database:

```sql
CREATE DATABASE student_db;
```

Create a dedicated database user and grant access to the project database.

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=student_api
DB_PASSWORD=your_password
DB_NAME=student_db
```

Never commit your `.env` file or expose database credentials publicly.

### 6. Create database tables

```bash
python create_tables.py
```

### 7. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to explore and test the available endpoints.

## Development Roadmap

- [x] Basic FastAPI application
- [x] RESTful CRUD endpoints using in-memory storage
- [x] MySQL database setup
- [x] SQLAlchemy database connection
- [x] Student ORM model
- [x] Pydantic schemas
- [x] Database table creation
- [ ] Database-backed CRUD operations
- [ ] Improved error handling and validation
- [ ] Authentication and authorization
- [ ] Automated API testing using Pytest
- [ ] Deployment

## Learning Objectives

This project is part of my backend development learning journey, focusing on:

- Understanding REST API architecture
- Working with HTTP methods and status codes
- Building APIs using FastAPI
- Database connectivity and SQL operations
- Understanding ORM concepts through SQLAlchemy
- Structuring maintainable backend applications

## License

This project is open-source and available under the MIT License.
