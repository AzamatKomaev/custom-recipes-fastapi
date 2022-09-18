from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from auth.jwt import get_current_user
from auth.schemas import TokenData
from core.database import get_db
from . import schemas
from . import services
from . import validator

router = APIRouter()


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schemas.UserCreate, db: Session = Depends(get_db)):
    user = await validator.verify_name_exist(db, request.name)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this name already exists in the system.",
        )

    new_user = await services.register_new_user(db, request)
    return new_user


@router.get('/', response_model=schemas.UserList)
async def get_all_users(db: Session = Depends(get_db)):
    return await services.get_all_users(db)


@router.get('/me', response_model=schemas.UserSingle)
async def get_me(db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return await services.get_user_by_id(db, current_user.id)


@router.get('/{user_id}', response_model=schemas.UserSingle)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return await services.get_user_by_id(db, user_id)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user(user_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    return await services.delete_user_by_id(db, user_id)
