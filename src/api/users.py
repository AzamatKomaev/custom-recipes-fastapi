import os
from fastapi import APIRouter


router = APIRouter(prefix='/users')


@router.get('/me')
def me():
    return {'user2': os.getenv('PGSQL_NAME')}
