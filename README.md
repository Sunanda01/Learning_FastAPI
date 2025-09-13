# Learning_FastAPI
A simple FastAPI project to learn & experiment with building REST APIs using Python and FastAPI.

## Features
- Basic CRUD / REST endpoints
- Use of FastAPI, Pydantic models
- Interactive API docs (Swagger UI / ReDoc)

## Installation

1. **Clone the repo**
   
   ```bash
   git clone https://github.com/Sunanda01/Learning_FastAPI.git
   cd Learning_FastAPI

2. **Create Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/Scripts/activate

3. **Install Dependencies**

   ```bash
   pip install fastapi uvicorn
   
4. **Start Server**
   ```bash
   uvicorn app.main:app --reload

## API Endpoints

| Method  | Endpoint            | Description            |
|---------|---------------------|------------------------|
| GET     | `/`                 | Health Check           |
| POST    | `/create-todo`      | Create Todo            |
| GET     | `/get-todo`         | Get All Todos          |
| GET     | `/todo/{id}`        | Get Todo by ID         |
| PUT     | `/update-todo/{id}` | Update Todo by ID      |
| DELETE  | `/del-todo/{id}`    | Delete Todo by ID      |
| DELETE  | `/delete-all`       | Delete All Todos       |

---

## 📑 API Documentation

FastAPI provides auto-generated interactive API docs:

- Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
---
