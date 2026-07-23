from datetime import datetime, timedelta, timezone
from jose import JWTError,jwt
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

#secret key

SECRET_KEY="your_secret_key_here_change_this"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

#create Access token

def create_access_token(data:dict):
    to_encode=data.copy()

    
    expire=datetime.now(timezone.utc)+timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp":expire})
    
    encoded_jwt=jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return encoded_jwt

#verify_access_token

def verify_access_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        user_id=payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data=schemas.TokenData(id=user_id)
    except JWTError:
        raise credentials_exception
    return token_data

#get current user

def get_current_user(
    token:str=Depends(oauth2_scheme),
    db:Session=Depends(get_db)
):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )
    
    token_data= verify_access_token(
        token,
        credentials_exception
                              )
    
    user= db.query(models.User).filter(
        models.User.id==token_data.id
    ).first()
    
    if user is None:
        raise credentials_exception
    return user