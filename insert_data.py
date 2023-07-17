from fastapi import APIRouter, HTTPException, Depends
from model import Users, Persons, session
from schema import User, Person
from typing import List
from create_token import decode_token, hash_password

insert = APIRouter(prefix="/add", tags=["add"], responses={404: {"detail": "No encontrado"}})

def save_users(users: List[User]):   
    new_users = [Users(username=u.username, password=hash_password(u.password), name=u.name, email=u.email, active=u.active) for u in users]
    session.add_all(new_users)
    session.commit()   

def save_persons(persons: List[Person]):
    new_persons = [Persons(dni=p.dni, paterno=p.paterno, materno=p.materno, nombre=p.nombre, nacimiento=p.nacimiento, ingreso=p.ingreso, cargo=p.cargo) for p in persons]
    session.add_all(new_persons)
    session.commit() 

@insert.post("/user")
def Add_user(user: User, response = Depends(decode_token)): 
    if response:
        save_users([user])
        return True
    
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})
    raise error
    
@insert.post("/users")
def Add_users(user: List[User], response = Depends(decode_token)):
    if response:
        save_users(user)
        return True
    
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})
    raise error

@insert.post("/person")
def Add_person(person: Person, response = Depends(decode_token)): 
    if response:
        save_persons([person])
        return True
    
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})
    raise error
    
@insert.post("/persons")
def Add_persons(person: List[Person], response = Depends(decode_token)):
    if response:
        save_persons(person)
        return True
    
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})
    raise error