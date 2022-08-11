import os
from dotenv import load_dotenv
from fastapi import FastAPI
from db.config import database
from db.models import users, recipes
from api.users import router as users_router


# load env variables from .env file.
load_dotenv()

# create tables from models.
users.Base.metadata.create_all(bind=database.engine)
recipes.Base.metadata.create_all(bind=database.engine)

# init application and include routers.
app = FastAPI()
app.include_router(users_router)


@app.get('/')
async def test():
    return {'pgsql_name': os.getenv('PGSQL_DB_NAME')}
