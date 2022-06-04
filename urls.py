from fastapi import APIRouter
from db.models import Field

router = APIRouter()


@router.post('/field/', response_model=Field)
async def create_field(field: Field):
    await field.save()
    return field
