"""
Tipos de dados customizados usados na aplicação.
"""
from typing import Dict, List, Union

EmployeeType = Dict[str, Union[float, int, str]]
EmployeeListType = List[EmployeeType]

UpdateEmployeeValuesType = Dict[str, Union[int, str]]