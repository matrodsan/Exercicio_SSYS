"""
Funções para o acesso ao banco de daados via SQLAlchemy via ORM ao
invés de consultas escritas diretamente em SQL.
"""
from typing import Generator

from sqlalchemy.orm import Session
from sqlalchemy.sql import func
import sqlalchemy as db

from .datatypes import UpdateEmployeeValuesType
from .models import Employee
from .schemas import CreateEmployeeSchema, EmployeeSchema

from datetime import date, datetime

employees = Employee


def create_employee(db: Session, employee: CreateEmployeeSchema):
    """
    Cria um novo empregado a partir dos dados enviados via API.
    """
    new_employee = Employee(**employee.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


def retrieve_all_employees(db: Session) -> Generator:
    """
    Retorna todos os registros dos empregados.
    """
    return db.query(employees).all()


def retrieve_employee(db: Session, employee_id: int):
    """
    Retorna o registro de um empregado a partir do seu _id_.
    """
    return db.query(employees).filter(employees.id == employee_id).first()


def retrieve_salaries(db: Session) -> Generator:
    """
    Retorna o registro dos empregados com maior e menor salário e a média de todos os salários.
    """
    return db.query(employees).order_by(employees.salary.desc()).first(), db.query(employees).order_by(employees.salary.asc()).first(), db.query(func.avg(employees.salary).label("average")).one()



def retrieve_birth_dates(db: Session) -> Generator:
    """
    Retorna o registro dos empregados com maior e menor idade e a média de todas as idades.
    """
    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    all_date_registers = db.query(employees.birth_date).all()
    ages = []
    for age in all_date_registers:
        ages.append(calculate_age(age[0]))
        print(age)

    age_avg = sum(ages)/len(ages)

    return db.query(employees).order_by(employees.birth_date.desc()).first(), db.query(employees).order_by(employees.birth_date.asc()).first(), age_avg


def update_employee(db: Session, employee_id: int, values: UpdateEmployeeValuesType):
    """
    Atualiza o registro de um empregado a partir do seu _id_ usando os
    novos valores em `values`.
    """
    if employee := retrieve_employee(db, employee_id):
        db.query(employees).filter(employees.id == employee_id).update(values)
        db.commit()
        db.refresh(employee)

        return employee


def remove_employee(db: Session, employee_id: int) -> bool:
    """
    Remove o registro de um empregado a partir do seu _id_.
    """
    if employee := retrieve_employee(db, employee_id):
        db.delete(employee)
        db.commit()

        return True
    
    return False