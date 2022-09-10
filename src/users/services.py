from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from . import models
from auth.hashing import get_password_hash


async def register_new_user(db: Session, request) -> models.User:
    new_user = models.User(name=request.name, password=get_password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_all_users(db: Session) -> List[models.User]:
    users = db.query(models.User).all()
    return users


async def get_user_by_id(db: Session, user_id: int) -> Optional[models.User]:
    user_info = db.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
    return user_info


async def get_user_by_name(db: Session, name: str) -> Optional[models.User]:
    user_info = db.query(models.User).filter(models.User.name == name).first()
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
    return user_info


async def delete_user_by_id(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
