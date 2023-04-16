#!/usr/bin/env python
# pyright: reportUntypedBaseClass=false

from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = "employee"

    first_name = Column(String)
    last_name = Column(String)
    salary = Column(Integer)
    bonus = Column(Integer)
    phone = Column(Integer)
    hire_date = Column(DateTime)
    role = Column(String)
    dept = Column(String, ForeignKey("department.name"))

    deptmnt = relationship("Department", back_populates="employee")

class Department(Base):
    __tablename__ = "department"

    name = Column(String)
    location = Column(String)

    employee = relationship("Employee", back_populates="deptmnt")
