# 📝 ToDo Manager API

A simple RESTful API written in Python using FastApi to work with tasks 

---

## 🚀 Features

 - Create a task
 - Get a list of all tasks
 - Get a single task by ID
 - Update a task
 - Delete a task

--- 

## 🛠️ Technologies Used

 - FastAPI - Modern, fast (high-performance) web framework for building APIs
 - Uvicorn - Lightning-fast ASGI server
 - SQLAlchemy - ORM for database interaction (optional)

---

## 📦 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/TheQuorix/ToDo-Manager.git
cd ToDo-Manager
```
2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate    # Linux / Mac
# or
.venv\Scripts\activate       # Windows
```
3. Install dependencies:
```bash
pip install fastapi, uvicorn, sqlalchemy
```
4. Run the server:
```bash
uvicorn main:app --reload
```
5. Open the documentation in your browser:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
