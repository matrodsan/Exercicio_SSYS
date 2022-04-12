from datetime import datetime
from typing import Dict, Generator

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from database.crud import (
    create_employee,
    remove_employee,
    retrieve_all_employees,
    retrieve_employee,
    update_employee,
    retrieve_salaries,
    retrieve_birth_dates,
)
from database.database import Base, SessionLocal, engine
from database.datatypes import EmployeeType
from database.schemas import CreateEmployeeSchema, EmployeeSchema, UpdateEmployeeSchema

from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBasic()

def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "ssys")
    correct_password = secrets.compare_digest(credentials.password, "testessys")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def get_db() -> Generator:
    """
    Retorna a sessão de conexão do banco de dados.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/employees", status_code=status.HTTP_200_OK, dependencies=[Depends(has_access)])
def get_all_employees(db: Session = Depends(get_db)) -> Generator:
    """
    Retorna todos os colaboradores armazenados.
    """
    if result := retrieve_all_employees(db):
        response = []
        for item in result:
            response.append({"id": item.id, "name": item.name, "email": item.email, "department": item.department, "salary": item.salary, "birth_date": item.birth_date.strftime("%d-%m-%Y")})
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem colaboradores cadastrados.",
    )


@app.get("/employees/{employee_id}/", status_code=status.HTTP_200_OK, dependencies=[Depends(has_access)])
def get_employee(employee_id: int, db: Session = Depends(get_db)) -> EmployeeType:
    """
    Retorna os dados do colaborador, recebe o _id_ do colaborador em `employee_id`
    e retorna as informações armazenadas ou gera uma exceção caso não seja
    encontrado.
    """
    if result := retrieve_employee(db, employee_id):
        response = {"id": result.id, "name": result.name, "email": result.email, "department": result.department, "salary": result.salary, "birth_date": result.birth_date.strftime("%d-%m-%Y")}
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Colaborador de 'id={employee_id}' não encontrado.",
    )


@app.delete("/employees/{employee_id}/", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(has_access)])
def delete_employee(employee_id: int, db: Session = Depends(get_db)) -> None:
    """
    Remove um colaborador do banco de dados, recebe o _id_ do colaborador em
    `employee_id` e retorna uma mensagem de sucesso, caso contrário gera uma
    exceção de não encontrado.
    """
    if not remove_employee(db, employee_id):

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Colaborador de 'id={employee_id}' não encontrado.",
        )


@app.post("/employees/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(has_access)])
def post_employee(employee: CreateEmployeeSchema, db: Session = Depends(get_db),) -> EmployeeType:
    """
    Insere um novo colaborador no banco de dados, recebe todos os campos
    necessários, valida e insere no banco de dados. Retorna o registro
    inserido acrescido do seu `id`.
    """
    if result := create_employee(db, employee):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


@app.put("/employees/{employee_id}/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(has_access)])
def put_employee(employee_id: int, employee: UpdateEmployeeSchema, db: Session = Depends(get_db),) -> EmployeeType:
    """
    Atualiza os dados de um colaborador, recebe o _id_  em `employee_id` e a
    lista de campos a modificar dentro do JSON (campos com valor `None`
    serão ignorados).
    """
    if result := update_employee(db, employee_id, {key: value for key, value in employee if value}):
        response = {"id": result.id, "name": result.name, "email": result.email, "department": result.department, "salary": result.salary, "birth_date": result.birth_date.strftime("%d-%m-%Y")}
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Colaborador de 'id={employee_id}' não encontrado.",
    )

@app.get("/employees/salary", status_code=status.HTTP_200_OK, dependencies=[Depends(has_access)])
def get_biggest_and_lowest_salary(db: Session = Depends(get_db)) -> Generator:
    """
    Retorna os colaboradores com maior e menor salário.
    """
    if result := retrieve_salaries(db):
        response_highest = {"id": result[0].id, "name": result[0].name, "email": result[0].email, "department": result[0].department, "salary": result[0].salary, "birth_date": result[0].birth_date.strftime("%d-%m-%Y")}
        response_lowest = {"id": result[1].id, "name": result[1].name, "email": result[1].email, "department": result[1].department, "salary": result[1].salary, "birth_date": result[1].birth_date.strftime("%d-%m-%Y")}
        report_salary = {"lowest": response_lowest, "highest": response_highest, "average": round(result[2].average,2)}
        return report_salary

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem colaboradores cadastrados.",
    )

@app.get("/employees/age", status_code=status.HTTP_200_OK, dependencies=[Depends(has_access)])
def get_younger_and_older_employee(db: Session = Depends(get_db)) -> Generator:
    """
    Retorna todos os colaboradores armazenados.
    """
    if result := retrieve_birth_dates(db):
        response_older = {"id": result[0].id, "name": result[0].name, "email": result[0].email, "department": result[0].department, "salary": result[0].salary, "birth_date": result[0].birth_date.strftime("%d-%m-%Y")}
        response_younger = {"id": result[1].id, "name": result[1].name, "email": result[1].email, "department": result[1].department, "salary": result[1].salary, "birth_date": result[1].birth_date.strftime("%d-%m-%Y")}
        report_age = {"younger": response_younger, "older": response_older, "average": round(result[2],2)}
        return report_age

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem colaboradores cadastrados.",
    )

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
