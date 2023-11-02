from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class CreateUserDependentDTO(BaseModel):
    name: str
    birth_date: date
    relationship: str
    cpf: str
    gender: str
    phone: str
    pensioner: Optional[str]


class CreateUserDTO(BaseModel):
    name: str
    address: str
    neighborhood: str
    city: str
    state: str
    zipcode: str
    cpf: str
    rg: str
    birth_date: date
    place_of_birth: str
    blood_type: str
    gender: str
    father_name: str
    mother_name: str
    position: str
    occupancy: str
    admission_date: date
    situation: str
    phone: str
    email: str
    marital_status: str
    education: str
    registration: str
    role: str
    category: str
    pattern: str
    dispatcher: str
    dispatched_date: date
    dependents: Optional[List[CreateUserDependentDTO]]
    workstation: Optional[str]
    nickname: Optional[str]
    password: str


class UpdateUserDTO(BaseModel):
    name: Optional[str]
    address: Optional[str]
    neighborhood: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zipcode: Optional[str]
    cpf: Optional[str]
    rg: Optional[str]
    birth_date: Optional[date]
    place_of_birth: Optional[str]
    blood_type: Optional[str]
    gender: Optional[str]
    father_name: Optional[str]
    mother_name: Optional[str]
    position: Optional[str]
    occupancy: Optional[str]
    admission_date: Optional[date]
    situation: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    marital_status: Optional[str]
    education: Optional[str]
    registration: Optional[str]
    role: Optional[str]
    category: Optional[str]
    pattern: Optional[str]
    dispatcher: Optional[str]
    dispatched_date: Optional[date]
    workstation: Optional[str]
    nickname: Optional[str]
    status: Optional[str]
    password: Optional[str]


class AuthUserDTO(BaseModel):
    registration: str
    password: str
