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
    fullName: str
    warName: Optional[str]
    registration: str
    birthDate: date
    rg: str
    cpf: str
    placeOfBirth: str
    ufNatural: str
    civilState: Optional[str]
    cep: str
    address: str
    number: Optional[str]
    neighborhood: str
    city: str
    complement: Optional[str]
    uf: str
    email: str
    cellphone: str
    phone: Optional[str]
    gender: str
    motherName: str
    fatherName: Optional[str]
    scolarity: Optional[str]
    religion: Optional[str]
    bloodType: Optional[str]
    actualWorkSituation: str
    admissionDate: date
    jobRole: str
    bodyOfLaw: str
    lotation: Optional[str]
    workPost: Optional[str]
    systemRole: Optional[str]
    dependents: Optional[List[CreateUserDependentDTO]]
    password: Optional[str]


class UpdateUserDTO(BaseModel):
    fullName: Optional[str]
    warName: Optional[str]
    registration: Optional[str]
    birthDate: Optional[date]
    rg: Optional[str]
    cpf: Optional[str]
    placeOfBirth: Optional[str]
    ufNatural: Optional[str]
    civilState: Optional[str]
    cep: Optional[str]
    address: Optional[str]
    number: Optional[str]
    neighborhood: Optional[str]
    city: Optional[str]
    uf: Optional[str]
    complement: Optional[str]
    email: Optional[str]
    cellphone: Optional[str]
    phone: Optional[str]
    gender: Optional[str]
    motherName: Optional[str]
    fatherName: Optional[str]
    scolarity: Optional[str]
    religion: Optional[str]
    bloodType: Optional[str]
    actualWorkSituation: Optional[str]
    admissionDate: Optional[date]
    bodyOfLaw: Optional[str]
    lotation: Optional[str]
    workPost: Optional[str]
    jobRole: Optional[str]
    systemRole: Optional[str]
    password: Optional[str]
