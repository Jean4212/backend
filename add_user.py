from fastapi import APIRouter, HTTPException, Depends
from model import Users, session
from schema import User
from typing import List
from create_token import decode_token

add_user = APIRouter(prefix="/adduser", tags=["user"], responses={404: {"detail": "No encontrado"}})

def save_users(users: List[User]):   
    new_users = [Users(username=u.username, password=u.password, name=u.name, email=u.email, active=u.active) for u in users]
    session.add_all(new_users)
    session.commit()      

@add_user.post("/")
def Add_user(user: User, response = Depends(decode_token)):
    error = HTTPException(status_code=400, detail="Datos invlidos")
    if user:
        save_users([user])
        return {"deatail": "ok"}
    raise error

@add_user.post("/add+")
def Add_users(user: List[User], response = Depends(decode_token)):
    error = HTTPException(status_code=400, detail="Datos invlidos")
    if user:
        save_users(user)
        return {"deatail": "ok"}
    raise error