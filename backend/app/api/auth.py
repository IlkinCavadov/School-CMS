from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserResponse, UserLogin
from app.services.auth_services import register_user, login_user
from app.db.dependencies import get_db
import jwt
from jwt.exceptions import InvalidTokenError
from app.settings.settings import settings
from fastapi import Depends,HTTPException, status
from app.repositories.user_repository import get_user_by_email
from app.schemas.auth import TokenData
from sqlalchemy.orm import Session
from app.schemas.auth import Token
from app.models.user import User
from app.auth.jwt import get_current_user
from app.services.auth_services import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role.name == "SuperAdmin":
        try:
            user = register_user(db, user_data)
            return user
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=403, detail="You do not have permission to register a new user.")



@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    try:
        user = login_user(db, user_data.email, user_data.password)

        access_token = create_access_token(
            data={"sub": user.email},
            expires_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        return Token(
            access_token=access_token,
            token_type="bearer"
        )

    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

