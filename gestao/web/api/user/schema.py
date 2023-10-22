from datetime import date
from typing import Optional

from pydantic import BaseModel


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
    mother_date: str
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
    mother_date: Optional[str]
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
