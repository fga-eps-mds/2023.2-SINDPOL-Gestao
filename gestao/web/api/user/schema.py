from datetime import date
from typing import List, Optional

from pydantic import BaseModel

from gestao.web.api.dependent.schema import CreateUserDependentDTO


class CreateUserDTO(BaseModel):
    registration: str
    password: str
    name: str
    war_name: str
    birth_date: date
    rg: str
    rg_consignor: str
    rg_date: date
    cpf: str
    place_of_birth: str
    marital_status: str
    zipcode: str
    address: str
    neighborhood: str
    city: str
    state: str
    email: str
    phone: str
    gender: str
    father_name: str
    mother_name: str
    education: str
    blood_type: str
    situation: str
    situation_obs: Optional[str]
    admission_date: Optional[date]
    role: Optional[str]
    position: Optional[str]
    occupancy: Optional[str]
    category: Optional[str]
    pattern: Optional[str]
    dispatcher: Optional[str]
    dispatched_date: Optional[date]
    dependents: Optional[List[CreateUserDependentDTO]]


class UpdateUserDTO(BaseModel):
    registration: Optional[str]
    password: Optional[str]
    name: Optional[str]
    war_name: Optional[str]
    birth_date: Optional[date]
    rg: Optional[str]
    rg_consignor: Optional[str]
    rg_date: Optional[date]
    cpf: Optional[str]
    place_of_birth: Optional[str]
    marital_status: Optional[str]
    zipcode: Optional[str]
    address: Optional[str]
    neighborhood: Optional[str]
    city: Optional[str]
    state: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    gender: Optional[str]
    father_name: Optional[str]
    mother_name: Optional[str]
    education: Optional[str]
    blood_type: Optional[str]
    situation: Optional[str]
    situation_obs: Optional[str]
    admission_date: Optional[date]
    role: Optional[str]
    position: Optional[str]
    occupancy: Optional[str]
    category: Optional[str]
    pattern: Optional[str]
    dispatcher: Optional[str]
    dispatched_date: Optional[date]


class AuthUserDTO(BaseModel):
    registration: str
    password: str
