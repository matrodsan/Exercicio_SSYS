from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.mysql import FLOAT
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    department = Column(String)
    salary = Column(FLOAT(precision=32, scale=2))
    birth_date = Column(Date)