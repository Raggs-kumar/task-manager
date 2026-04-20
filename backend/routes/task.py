from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from deps import get_current_user
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

# CREATE TASK
@router.post("/tasks")
def create_task(task: schemas.TaskCreate,
                db: Session = Depends(get_db),
                user_id: int = Depends(get_current_user)):
    new_task = models.Task(title=task.title, user_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# GET ALL TASKS
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db),
              user_id: int = Depends(get_current_user)):
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()

# UPDATE TASK
@router.put("/tasks/{task_id}")
def update_task(task_id: int,
                update: schemas.TaskUpdate,
                db: Session = Depends(get_db),
                user_id: int = Depends(get_current_user)):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == user_id
    ).first()

    if not task:
        raise HTTPException(404, "Task not found")

    task.completed = update.completed
    db.commit()

    return {"message": "Task updated"}

# DELETE TASK
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int,
                db: Session = Depends(get_db),
                user_id: int = Depends(get_current_user)):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == user_id
    ).first()

    if not task:
        raise HTTPException(404, "Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}