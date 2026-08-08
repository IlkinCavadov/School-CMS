import jwt
from typing import Annotated
from jwt.exceptions import InvalidTokenError
from app.settings.settings import settings
from fastapi import Depends,HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.db.dependencies import get_db
from app.repositories.user_repository import get_user_by_email
from app.schemas.auth import TokenData
from sqlalchemy.orm import Session


bearer_scheme = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
        db: Session = Depends(get_db)
    ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(credentials.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

  