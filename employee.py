from fastapi import APIRouter, HTTPException, Depends
from model import Persons, session
from create_token import decode_token

route_staff = APIRouter(tags=["Employee"], responses={404: {"detail": "No encontrado"}})

def http_error(code: int, message: str):
    return HTTPException(status_code=code, detail=message, headers={"WWW-Authenticate": "Bearer"})

@route_staff.get("/empleado")
def employee(dni: str, response = Depends(decode_token)):
    if response:
        person = session.query(Persons).where(Persons.dni == dni).all() 

        if person:
            return person[0]
        
        return False    
    
    raise http_error(401, "Token Invalido") 

@route_staff.get("/empleados")
def employees(response = Depends(decode_token)):
    if response:
        persons = session.query(Persons).all()          
        return persons       
   
    raise http_error(401, "Token Invalido")
