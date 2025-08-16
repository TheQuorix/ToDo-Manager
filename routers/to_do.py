from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Task
from database.schemas import TaskCreate, Task as dbTask


router = APIRouter()


@router.get("/tasks")
async def get_tasks(db: Session = Depends(get_db)):
    if db.query(Task).all():
        return db.query(Task).all()
    
    return {"message": "Записи не найдены"}


@router.get("/tasks/{id}")
async def get_tasks(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).get(id)
    if task:
        return task
    
    return {"message": "Запись не найдена"}


@router.post("/tasks")
async def create_task(task: TaskCreate, db: Session = Depends(get_db)) -> dbTask:
    db_task = Task(text=task.text)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    
    return db_task


@router.put("/tasks/{id}")
async def update_task(id: int, text: str, db: Session = Depends(get_db)):
    task = db.query(Task).get(id)
    if task:
        task.text = text
        db.commit()
        db.refresh(task)
        return task

    return {"message": "Запись не найдена"}


@router.delete("/tasks/{id}")
async def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).get(id)
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Запись успешна удалена"}
    return {"message": "Запись не найдена"}