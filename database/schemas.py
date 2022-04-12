"""
Leiaute dos dados utilizados pelo pydantic para validação dos mesmos.
"""
import re
from typing import Any
import datetime
from pydantic import BaseModel, validator, EmailStr

BIRTH_DATE_REGEX = re.compile('^([0-2][0-9]|(3)[0-1])(-)(((0)[0-9])|((1)[0-2]))(-)\d{4}$')

class EmployeeBaseSchema(BaseModel):
    """
    Define a estrura de dados que armazena as informações dos colaboradores.
    """
    name: str
    email: EmailStr
    department: str
    salary: float
    birth_date: str

    @validator("birth_date", allow_reuse=True)
    def validate_birth_date(cls, v: str, **kwargs: int) -> str:
        """
        Verifica se a data tem o formato correto
        """
        if not BIRTH_DATE_REGEX.match(birth_date := v.rjust(10, "0")):
            raise ValueError("A DATA informada é inválida!")

        return datetime.datetime.strptime(birth_date,"%d-%m-%Y").date()



class CreateEmployeeSchema(EmployeeBaseSchema):
    def employee():
        return True

class EmployeeSchema(EmployeeBaseSchema):
    """
    Esquema de dados para ser usado para visualização dos colaboradores.
    """
    id: int


class UpdateEmployeeSchema(EmployeeBaseSchema):
    """
    Esquema de dados para a atualização dos dados dos estudantes.
    """
    name: str = ""
    email: str  = ""
    department: str  = ""
    salary: str  = ""
    birth_date: str  = ""
