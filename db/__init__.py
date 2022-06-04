from .connection import metadata, engine
from .models import Field  # noqa 401

metadata.create_all(engine)
