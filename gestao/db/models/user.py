from datetime import date, datetime

import ormar

from gestao.db.base import BaseMeta


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: str = ormar.String(max_length=200, primary_key=True)
    fullName: str = ormar.String(max_length=200)
    warName: str = ormar.String(max_length=200, nullable=True)
    registration: str = ormar.String(max_length=200, unique=True)
    birthDate: date = ormar.Date()
    rg: str = ormar.String(max_length=200, unique=True)
    cpf: str = ormar.String(max_length=200, unique=True)
    placeOfBirth: str = ormar.String(max_length=200)
    ufNatural: str = ormar.String(max_length=100)
    civilState: str = ormar.String(max_length=200, nullable=True)
    cep: str = ormar.String(max_length=100)
    address: str = ormar.String(max_length=200)
    number: str = ormar.String(max_length=100, nullable=True)
    neighborhood: str = ormar.String(max_length=100, nullable=True)
    city: str = ormar.String(max_length=100)
    complement: str = ormar.String(max_length=200, nullable=True)
    uf: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=200)
    cellphone: str = ormar.String(max_length=200)
    phone: str = ormar.String(max_length=200, nullable=True)
    gender: str = ormar.String(max_length=200)
    motherName: str = ormar.String(max_length=200)
    fatherName: str = ormar.String(max_length=200, nullable=True)
    scolarity: str = ormar.String(max_length=200, nullable=True)
    religion: str = ormar.String(max_length=200, nullable=True)
    bloodType: str = ormar.String(max_length=200, nullable=True)
    actualWorkSituation: str = ormar.String(max_length=200)
    admissionDate: date = ormar.Date()
    jobRole: str = ormar.String(max_length=200, nullable=True)
    bodyOfLaw: str = ormar.String(max_length=200)
    lotation: str = ormar.String(max_length=200, nullable=True)
    workPost: str = ormar.String(max_length=200, nullable=True)
    systemRole: str = ormar.String(max_length=200, nullable=True)
    password: str = ormar.String(max_length=200, nullable=True)
    status: str = ormar.String(max_length=200, default="active")
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
    updated_at: datetime = ormar.DateTime(
        timezone=True,
        default=datetime.now,
        onupdate=datetime.now,
    )
