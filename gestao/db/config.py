from databases import Database

from gestao.settings import settings

database = Database(str(settings.db_url))
