from datetime import date, datetime
from typing import Optional
from gestao.db.base import BaseMeta
import ormar

class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: str = ormar.String(max_length=200, primary_key=True)
    fullName: str = ormar.String(max_length=200)
    warName: Optional[str] = ormar.String(max_length=200, unique=True, nullable=True)
    registration: str = ormar.String(max_length=200, unique=True)
    birthDate: date = ormar.Date()
    rg: str = ormar.String(max_length=200, unique=True)
    cpf: str = ormar.String(max_length=200, unique=True)
    placeOfBirth: str = ormar.String(max_length=200)
    ufNatural: str = ormar.String(max_length=100)
    marital_status: str = ormar.String(max_length=200)
    zipcode: str = ormar.String(max_length=100)
    address: str = ormar.String(max_length=200)
    number: str = ormar.String(max_length=100)
    city: str = ormar.String(max_length=100)
    uf: str = ormar.String(max_length=100)
    complement: str = ormar.String(max_length=200)
    email: str = ormar.String(max_length=200)
    cellphone: str = ormar.String(max_length=200)
    phone: str = ormar.String(max_length=200)
    gender: str = ormar.String(max_length=200)
    motherName: str = ormar.String(max_length=200)
    fatherName: str = ormar.String(max_length=200)
    scolarity: str = ormar.String(max_length=200)
    religion: str = ormar.String(max_length=200)
    bloodType: str = ormar.String(max_length=200)
    function: str = ormar.String(max_length=200)
    actualSituation: str = ormar.String(max_length=200)
    admissionDate: date = ormar.Date()
    role: str = ormar.String(max_length=200)
    bodyOfLaw: str = ormar.String(max_length=200)
    lotation: str = ormar.String(max_length=200)
    workstation: Optional[str] = ormar.String(max_length=200, nullable=True)
    
    status: str = ormar.String(max_length=200, default="active")
    dispatcher: str = ormar.String(max_length=200)
    dispatched_date: date = ormar.Date()
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
    updated_at: datetime = ormar.DateTime(
        timezone=True,
        default=datetime.now,
        onupdate=datetime.now,
    )
