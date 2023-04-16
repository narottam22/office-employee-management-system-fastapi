#!/usr/bin/env python 
# pyright: reportOptionalMemberAccess=false


from sqlalchemy.orm import Session
import models, schemas
import datetime


def employee_creation(employee_create: schemas.EmployeeCreate, db: Session):
    '''Creates a employee record in database'''

    db_employee_create = models.Employee(first_name=employee_create.first_name, \
                        last_name=employee_create.last_name, salary=employee_create.salary, \
                        bonus=employee_create.bonus, phone=employee_create.phone, created_at=datetime.datetime.now(), \
                        role=employee_create.role, dept=employee_create.department)
    
    db.add(db_employee_create)
    db.commit()
    db.refresh(db_employee_create)
    return db_employee_create

def get_employee_by_id(id: int, db: Session):
    '''Fetches the employee record from database'''

    db_employee=db.query(models.Employee).filter(models.Employee.id == id).first()

    return db_employee
