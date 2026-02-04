from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: str
    major: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        from_attributes = True

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    major: Optional[str] = None