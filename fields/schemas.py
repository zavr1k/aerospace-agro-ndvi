from pydantic import BaseModel, Field

from geojson_pydantic import Feature


class CreateField(BaseModel):
    name: str = Field(max_length=120)
    geojson: Feature
