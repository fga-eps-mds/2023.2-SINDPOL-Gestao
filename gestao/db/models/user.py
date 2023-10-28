from datetime import date, datetime

import ormar

from gestao.db.base import BaseMeta


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: str = ormar.String(max_length=200, primary_key=True)
    registration: str = ormar.String(max_length=200, unique=True)
    password: str = ormar.String(max_length=200)
    name: str = ormar.String(max_length=200)
    war_name: str = ormar.String(max_length=200)
    birth_date: date = ormar.Date()
    rg: str = ormar.String(max_length=200, unique=True)
    rg_consignor: str = ormar.String(max_length=100)
    rg_date: date = ormar.Date()
    cpf: str = ormar.String(max_length=200, unique=True)
    place_of_birth: str = ormar.String(max_length=200)
    marital_status: str = ormar.String(max_length=200)
    zipcode: str = ormar.String(max_length=100)
    address: str = ormar.String(max_length=200)
    neighborhood: str = ormar.String(max_length=200)
    city: str = ormar.String(max_length=100)
    state: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=200)
    phone: str = ormar.String(max_length=200)
    gender: str = ormar.String(max_length=200)
    father_name: str = ormar.String(max_length=200)
    mother_name: str = ormar.String(max_length=200)
    education: str = ormar.String(max_length=200)
    blood_type: str = ormar.String(max_length=200)
    situation: str = ormar.String(max_length=200)
    situation_obs: str = ormar.String(max_length=300)
    admission_date: date = ormar.Date()
    role: str = ormar.String(max_length=200)
    position: str = ormar.String(max_length=200)
    occupancy: str = ormar.String(max_length=200)
    category: str = ormar.String(max_length=200)
    pattern: str = ormar.String(max_length=200)
    dispatcher: str = ormar.String(max_length=200)
    dispatched_date: date = ormar.Date()
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
    updated_at: datetime = ormar.DateTime(
        timezone=True,
        default=datetime.now,
        onupdate=datetime.now,
    )
