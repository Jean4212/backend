from fastapi import APIRouter, HTTPException, Depends
from model import Persons, Calendars, session
from create_token import decode_token

select = APIRouter(prefix="/select", tags=["select"], responses={404: {"detail": "No encontrado"}})

@select.get("/person")
def Get_person(dni: str, response = Depends(decode_token)):
    if response:
        person = session.query(Persons).where(Persons.dni == dni).all() 

        if person:
            return person[0]
        
        return False
    
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})  
    raise error

@select.get("/persons")
def Get_persons(response = Depends(decode_token)):
    if response:
        persons = session.query(Persons).all()  
        return persons  
     
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})  
    raise error

@select.get("/car")
def Get_car(unidad: str, response = Depends(decode_token)):
    if response:
        car = session.query(Calendars).where(Calendars.unidad == unidad).all() 

        if car:
            return car[0]
        
        return False
    
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})  
    raise error

@select.get("/cars")
def Get_cars(response = Depends(decode_token)):
    if response:
        cars = session.query(Calendars).all()  
        return cars  
     
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})  
    raise error

    
