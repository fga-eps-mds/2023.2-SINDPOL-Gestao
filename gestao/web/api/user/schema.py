from datetime import date
from typing import List, Optional

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


class CreateUserDTO(BaseModel):
    name: str
    war_name: str
    password: str
    address: str
    neighborhood: str
    city: str
    state: str
    zipcode: str
    cpf: str
    rg: str
    rg_consignor: str
    rg_date: date
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
    situation_obs: Optional[str]
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


class UpdateUserDTO(BaseModel):
    name: Optional[str]
    war_name: Optional[str]
    password: Optional[str]
    address: Optional[str]
    neighborhood: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zipcode: Optional[str]
    cpf: Optional[str]
    rg: Optional[str]
    rg_consignor: Optional[str]
    rg_date: Optional[date]
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
    situation_obs: Optional[str]
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


class AuthUserDTO(BaseModel):
    registration: str
    password: str
