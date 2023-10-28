from datetime import date, datetime

import ormar

from gestao.db.base import BaseMeta
from gestao.db.models.user import User


class Dependent(ormar.Model):
    class Meta(BaseMeta):
        tablename = "dependent"

    id: str = ormar.String(max_length=200, primary_key=True)
    user_id: User = ormar.ForeignKey(User, ondelete=ormar.ReferentialAction.CASCADE)
    name: str = ormar.String(max_length=200)
    cpf: str = ormar.String(max_length=200, unique=True)
    birth_date: date = ormar.Date()
    gender: str = ormar.String(max_length=200)
    relationship: str = ormar.String(max_length=200)
    phone: str = ormar.String(max_length=200)
    deceased: bool = ormar.Boolean(default=False)
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
    updated_at: datetime = ormar.DateTime(
        timezone=True,
        default=datetime.now,
        onupdate=datetime.now,
    )
