from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from . import models
from . import schemas
from auth.hashing import get_password_hash


async def register_new_user(db: Session, request) -> models.User:
    new_user = models.User(name=request.name, password=get_password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_all_users(db: Session) -> schemas.UserList:
    users = db.query(models.User).all()
    users_model = []
    for user in users:
        users_model.append(schemas.UserSingle(**user.__dict__, recipes_count=len(user.recipes)))
    return schemas.UserList(__root__=users_model)


async def get_user_by_id(db: Session, user_id: int) -> schemas.UserSingle:
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
    return schemas.UserSingle(**user.__dict__, recipes_count=len(user.recipes))


async def delete_user_by_id(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
