from fastapi import APIRouter, HTTPException, Depends
from model import Users, Persons, session
from schema import User, Person
from typing import List
from create_token import decode_token

route2 = APIRouter(prefix="/user", tags=["User"])

@route2.get("/")
def get_user(username: str, response = Depends(decode_token)):    

    if response:

        user_db = session.query(Users).filter(Users.username == username).all()

        if user_db:      
            for u in user_db:                  
                del u.__dict__["password"] # Otra alternativa: u.__dict__.pop("password")  

            return user_db[0]
        error = HTTPException(status_code=400, detail="Usuario invalido")
        raise error
    error = HTTPException(status_code=401, detail="Token invalido")
    raise error
    

@route2.get("/me")   
def index():    
    
    return False



@route2.get("/users")
def get_users():
    
    users = session.query(Users).all()   
    myArray = []

    if users:     
        for user in users:
            myArray.append(user)

    return myArray   

@route2.post("/users")
def post_users(users: List[User]):
    
    new_users = [Users(name=u.name, username=u.username, password=u.password) for u in users]
    session.add_all(new_users)
    session.commit()      
   
    return True

@route2.delete("/users")
def delete_users():
    
    session.execute(Users.__table__.delete())
    session.commit()
   
    return True

@route2.get("/persons")
def get_persons():

    persons = session.query(Persons).all() 
    myArray = []

    if persons:
        for person in persons:
            myArray.append(person)

    return myArray   

@route2.post("/persons")
def post_persons(persons: List[Person]):
   
    new_persons = [Persons(dni=p.dni, paterno=p.paterno, materno=p.materno, nombre=p.nombre, nacimiento=p.nacimiento, 
                           ingreso=p.ingreso, cargo=p.cargo) for p in persons]    
    session.add_all(new_persons)
    session.commit()      
   
    return True

@route2.delete("/persons")
def delete_persons():
        
    session.execute(Persons.__table__.delete())
    session.commit()
   
    return True
