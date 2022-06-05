import uvicorn
from fastapi import FastAPI

from db.connection import database
from fields.api import router


app = FastAPI(title="NDVI")
app.include_router(router, prefix="/fields")


@app.on_event('startup')
async def startup() -> None:
    database_ = app.state.database = database
    if not database_.is_connected:
        await database_.connect()


@app.on_event('shutdown')
async def shutdown() -> None:
    database_ = app.state.database = database
    if database_.is_connected:
        await database_.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, host='0.0.0.0', reload=True)
