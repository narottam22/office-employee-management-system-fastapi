#!/usr/bin/env python 
# pyright: reportOptionalMemberAccess=false, reportGeneralTypeIssues= false


from sqlalchemy.orm import Session
import models, schemas
import datetime


def employee_creation(employee_create: schemas.EmployeeCreate, db: Session):
    '''Creates a employee record in database'''

    db_employee_create = models.Employee(first_name=employee_create.first_name, \
                        last_name=employee_create.last_name, salary=employee_create.salary, \
                        bonus=employee_create.bonus, phone=employee_create.phone, created_at=datetime.datetime.now(), \
                        role=employee_create.role, dept=employee_create.dept)
    
    db.add(db_employee_create)
    db.commit()
    db.refresh(db_employee_create)
    return db_employee_create

def get_employee_by_id(id: int, db: Session):
    '''Fetches the employee record from database'''

    db_employee=db.query(models.Employee).filter(models.Employee.id == id).first()

    return db_employee

def edit_employee(id: int, employee_edit: schemas.EmployeeCreate, db: Session):
    '''Updates a employee record in database'''
    db_employee_edit=db.query(models.Employee).filter(models.Employee.id == id).first()

    if employee_edit.first_name:
        db_employee_edit.first_name=employee_edit.first_name

    if employee_edit.last_name:
        db_employee_edit.last_name=employee_edit.last_name

    if employee_edit.salary:
        db_employee_edit.salary=employee_edit.salary

    if employee_edit.bonus:
        db_employee_edit.bonus=employee_edit.bonus

    if employee_edit.phone:
        db_employee_edit.phone=employee_edit.phone

    if employee_edit.role:
        db_employee_edit.role=employee_edit.role
    
    if employee_edit.dept:
        db_employee_edit.dept=employee_edit.dept

    db.commit()

    return db_employee_edit

def delete_employee(id: int, db: Session):
    '''Removes an employee record from database'''
    db_employee=db.query(models.Employee).filter(models.Employee.id == id).first()
    db.delete(db_employee)
    db.delete(db_employee)
    db.commit()
    return "Employee Record Deleted Successfully"