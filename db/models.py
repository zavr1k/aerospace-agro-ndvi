import ormar

from db.connection import database, metadata


class Field(ormar.Model):
    class Meta(ormar.ModelMeta):
        tablename = 'fields'
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    name: str = ormar.String(max_length=180)
    geojson = ormar.JSON()
