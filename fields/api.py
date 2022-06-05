from fastapi import APIRouter

from db.models import Field
from .schemas import CreateField

router = APIRouter()


@router.post("/create")
async def create_field(field: CreateField) -> Field:
    return await Field.objects.create(**field.dict())


@router.get("/{pk}")
async def get_field(pk: int) -> Field:
    return await Field.objects.get(id=pk)
