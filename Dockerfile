FROM fnndsc/python-poetry:1.1.13

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry install