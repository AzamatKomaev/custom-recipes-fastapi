from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from users.models import User
from core.database import get_db
from . import hashing
from .jwt import create_access_token

router = APIRouter()


@router.post('/login')
def login(db: Session = Depends(get_db), request: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    # Generate a JWT Token
    access_token = create_access_token(data={"sub": user.name})

    return {"access_token": access_token, "token_type": "bearer"}
