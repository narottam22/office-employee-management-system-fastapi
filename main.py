#!/usr/bin/env python

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from typing import Optional

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    ''' Get a database session from the session'''
    # db initialized to None
    db: Optional[Session] = None

    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()


@app.post("/create_employee", response_model=schemas.EmployeeResponse)
async def create_employee_record(employee_create: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    '''Creates a new employee record'''

    try:
        db_employee = crud.employee_creation(employee_create, db)

        return db_employee
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e.__class__.__name__))


@app.get("/employee/{id}", response_model=schemas.EmployeeResponse)
async def get_employee_record(id: int, db: Session = Depends(get_db)):
    '''Returns the record of employee by id'''

    try:
        db_employee = crud.get_employee_by_id(id, db)

        return db_employee
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e.__class__.__name__))
    
@app.put("/employee/{id}", response_model=schemas.EmployeeResponse)
async def update_employee_record(id: int, employee_update: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    '''Returns the record of employee by id'''

    try:
        db_employee = crud.edit_employee(id, employee_update, db)

        return db_employee
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e.__class__.__name__))
    
@app.delete("/employee/{id}")
async def remove_employee_record(id: int, db: Session = Depends(get_db)):
    '''Returns the record of employee by id'''

    try:
        db_employee = crud.delete_employee(id, db)

        return db_employee
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e.__class__.__name__))