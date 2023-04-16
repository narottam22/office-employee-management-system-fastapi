from typing import  Optional
from pydantic import BaseModel
from datetime import  time

class EmployeeCreate(BaseModel):
    '''Pydantic model for Creating an employee record'''
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    salary: Optional[int] = None
    bonus: Optional[int] = None
    phone: Optional[str] = None
    role: Optional[str] = None
    department: Optional[str] = None

    class Config:
        orm_mode = True


class EmployeeResponse(BaseModel):
    '''Pydantic Model for Employee response'''
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    salary: Optional[int] = None
    bonus: Optional[int] = None
    phone: Optional[str] = None
    created_at: Optional[time] = None
    role: Optional[str] = None
    department: Optional[str] = None

    class Config:
        orm_mode = True