from datetime import date, datetime
from typing import Optional

import ormar

from gestao.db.base import BaseMeta


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: str = ormar.String(max_length=200, primary_key=True)
    name: str = ormar.String(max_length=200)
    address: str = ormar.String(max_length=200)
    neighborhood: str = ormar.String(max_length=200)
    city: str = ormar.String(max_length=100)
    state: str = ormar.String(max_length=100)
    zipcode: str = ormar.String(max_length=100)
    cpf: str = ormar.String(max_length=200, unique=True)
    rg: str = ormar.String(max_length=200, unique=True)
    birth_date: date = ormar.Date()
    place_of_birth: str = ormar.String(max_length=200)
    blood_type: str = ormar.String(max_length=200)
    gender: str = ormar.String(max_length=200)
    father_name: str = ormar.String(max_length=200)
    mother_name: str = ormar.String(max_length=200)
    position: str = ormar.String(max_length=200)
    occupancy: str = ormar.String(max_length=200)
    admission_date: date = ormar.Date()
    situation: str = ormar.String(max_length=200)
    phone: str = ormar.String(max_length=200)
    email: str = ormar.String(max_length=200)
    marital_status: str = ormar.String(max_length=200)
    education: str = ormar.String(max_length=200)
    registration: str = ormar.String(max_length=200, unique=True)
    role: str = ormar.String(max_length=200)
    category: str = ormar.String(max_length=200)
    pattern: str = ormar.String(max_length=200)
    status: str = ormar.String(max_length=200, default="active")
    workstation: Optional[str] = ormar.String(max_length=200, nullable=True)
    nickname: Optional[str] = ormar.String(max_length=200, unique=True, nullable=True)
    password: str = ormar.String(max_length=200, nullable=True)
    religion: Optional[str] = ormar.String(max_length=200, nullable=True)
    dispatcher: str = ormar.String(max_length=200)
    dispatched_date: date = ormar.Date()
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
    updated_at: datetime = ormar.DateTime(
        timezone=True,
        default=datetime.now,
        onupdate=datetime.now,
    )
