from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from db.models import Field
from .schemas import CreateField
from .services import get_field_image, get_ndvi_image

router = APIRouter()


@router.get("/", response_model=list[Field])
async def get_fields() -> list[Field]:
    return await Field.objects.all()


@router.get("/{pk}")
async def get_field_by_id(pk: int) -> Field:
    field = await Field.objects.get_or_none(id=pk)
    if not field:
        raise HTTPException(status_code=404, detail='Item not found')
    return field


@router.post("/create")
async def create_field(field: CreateField) -> Field:
    return await Field.objects.create(**field.dict())


@router.delete("/{pk}/delete")
async def delete_field(pk: int) -> None:
    return await Field.objects.delete(id=pk)


@router.post('/{pk}/image')
async def get_image(pk: int) -> Response:
    field = await Field.objects.get_or_none(id=pk)
    if not field:
        raise HTTPException(status_code=404, detail='Item not found')
    image_data = get_field_image(field)
    return Response(image_data, media_type='image/png')


@router.post('/{pk}/ndvi')
async def get_ndvi(pk: int) -> Response:
    field = await Field.objects.get_or_none(id=pk)
    if not field:
        raise HTTPException(status_code=404, detail='Item not found')
    ndvi_image_data = get_ndvi_image(field)
    return Response(ndvi_image_data, media_type='image/png')
