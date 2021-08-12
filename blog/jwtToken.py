from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
import schemas

SECRET_KEY = "HelloWorld123456789"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30

def create_access_token(
    data : schemas.TokenData,
    expires_delta : Optional[timedelta] = None 
) :
    to_encode = data.copy()
    if expires_delta :
        expire = datetime.utcnow() + expires_delta
    else :
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt