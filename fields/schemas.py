from geojson_pydantic.geometries import Polygon
from pydantic import BaseModel, Field


class CreateField(BaseModel):
    name: str = Field(max_length=120)
    geojson: Polygon
