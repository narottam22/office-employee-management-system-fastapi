#!/usr/bin/env python

from sqlalchemy import Integer, String, Column, Time
from database import Base

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    salary = Column(Integer)
    bonus = Column(Integer)
    phone = Column(String)
    created_at= Column(Time)
    role = Column(String)
    dept = Column(String)