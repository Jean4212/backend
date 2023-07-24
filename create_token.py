from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from model import session, Users

SECRET = "09d25e094faa6ca00uuyghjhgjfc818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
EXPIRE = 24

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])

def get_user(username: str):
    user_db = session.query(Users).where(Users.username == username).all()
    if user_db:
        return user_db[0]
    
    return False

def encode_token(username: str):   
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(hours=EXPIRE)}
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)

    return token

def decode_token(token: str = Depends(oauth2)):       
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            return False  
              
    except JWTError:      
        return False 
    
    user = get_user(username)
    if user:
        del user.__dict__["password"]   
        return user
    
    return False

def verify_password(password: str, hash: str):
    return crypt.verify(password, hash)

def hash_password(password: str):
    return crypt.hash(password)
