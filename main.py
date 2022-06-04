import uvicorn
from fastapi import FastAPI

from db.connection import database
import urls


app = FastAPI()
app.include_router(urls.router)


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


@app.get('/')
async def home():
    response = 'Hello world!'
    return {'key': response}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, host='0.0.0.0', reload=True)
