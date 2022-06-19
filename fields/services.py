import ee
import requests
from db.models import Field


def get_field_image(field: Field) -> bytes:
    start_date = '2021-05-01'
    end_date = '2021-06-30'
    image = _get_ee_image(field, start_date, end_date)
    rgb_image = image.visualize(min=0, max=2000, bands=['B4', 'B3', 'B2'])
    url = _get_thumbnail_url(rgb_image)
    data = requests.get(url).content
    return data


def get_ndvi_image(field: Field) -> bytes:
    start_date = '2021-05-01'
    end_date = '2021-06-30'
    image = _get_ee_image(field, start_date, end_date)
    ndvi = image.normalizedDifference(['B8', 'B4'])
    ndvi_params = {
        'palette': ['#ffffcc',
                    '#c2e699',
                    '#78c679',
                    '#31a354',
                    '#006837'],
        'max': 1,
        'min': 0
    }
    ndvi_image = ndvi.visualize(**ndvi_params)
    url = _get_thumbnail_url(ndvi_image)
    return requests.get(url).content


def _get_ee_image(field: Field, start_date: str, end_date: str)\
        -> ee.Image:

    area = ee.Geometry(field.geojson)
    image = ee.ImageCollection('COPERNICUS/S2_SR') \
        .filterBounds(area) \
        .filterDate(start_date, end_date) \
        .sort('CLOUDY_PIXEL_PERCENTAGE') \
        .first() \
        .clip(area)
    return image


def _get_thumbnail_url(image: ee.Image) -> str:
    return image.getThumbURL(
        params={'format': 'png', 'dimensions': '256x256'}
    )
