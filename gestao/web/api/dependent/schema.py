from datetime import date
from typing import Optional

from pydantic import BaseModel


class CreateUserDependentDTO(BaseModel):
    name: str
    cpf: str
    birth_date: date
    gender: str
    relationship: str
    deceased: bool


class UpdateUserDependentDTO(BaseModel):
    name: Optional[str]
    cpf: Optional[str]
    birth_date: Optional[date]
    gender: Optional[str]
    relationship: Optional[str]
    deceased: Optional[bool]

