from pydantic import BaseModel


class TaskBase(BaseModel):
    text: str


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    
    class Config:
        from_attributes = True