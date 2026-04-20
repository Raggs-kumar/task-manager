from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str   # can also send email
    password: str

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    completed: bool

class TaskOut(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True