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
    birth_date: date = ormar.Date()
    relationship: str = ormar.String(max_length=200)
    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
    updated_at: datetime = ormar.DateTime(
        timezone=True,
        default=datetime.now,
        onupdate=datetime.now,
    )
