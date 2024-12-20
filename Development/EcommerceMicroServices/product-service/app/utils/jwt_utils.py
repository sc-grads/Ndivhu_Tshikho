# app/jwt_utils.py
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

SECRET_KEY = "your_secret_key"  # Use the same secret key as in user-service
ALGORITHM = "HS256"

class TokenData:
    username: str
    role: str

def decode_token(token: str, db: Session):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None or role is None:
            raise credentials_exception
        return TokenData(username=email, role=role)
    except JWTError:
        raise credentials_exception
