from ormar import ModelMeta

from gestao.db.config import database
from gestao.db.meta import meta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta
