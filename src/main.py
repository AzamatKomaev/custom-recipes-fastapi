from fastapi import FastAPI
from api import users

app = FastAPI()
app.include_router(users.router)


@app.get('/')
async def test():
    return {'hello': 'world'}
