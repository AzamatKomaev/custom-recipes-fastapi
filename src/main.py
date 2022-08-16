import os
from dotenv import load_dotenv
from fastapi import FastAPI
from api.users import router as users_router


# load env variables from .env file.
load_dotenv()

# init application and include routers.
app = FastAPI()
app.include_router(users_router)


@app.get('/')
async def test():
    return {'pgsql_name': os.getenv('PGSQL_DB_NAME')}
