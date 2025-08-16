# 📝 ToDo Manager API

<img width="1920" height="947" alt="изображение" src="https://github.com/user-attachments/assets/d8e94f20-1375-4bd6-bc75-7fbe4c25aea0" />

A simple RESTful API for managing tasks (CRUD operations) built with **FastAPI** and **Python**. 

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

---

## 🗂️ Project Structure
```
.
├── database/
│   ├── __init__.py
│   ├── database.py # Database connection setup
│   ├── models.py # Task SQLAlchemy model
│   └── schemas.py # Pydantic schemas
├── routers/
│   └── to_do.py # Handles all API endpoints for managing tasks (Create, Read, Update, Delete).
├── main.py # Entry of the application
```

---

🚧 Future Improvements
 - User authentication
 - Task filtering (by status, date, etc.)
