import ormar

from db.connection import database, metadata


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Field(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'fields'

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    name: str = ormar.String(max_length=180)
