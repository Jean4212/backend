from fastapi import APIRouter, HTTPException, Depends
from model import Schedules, session
from create_token import decode_token

route_calendar = APIRouter(tags=["Schedule"], responses={404: {"detail": "No encontrado"}})

def http_error(code: int, message: str):
    return HTTPException(status_code=code, detail=message, headers={"WWW-Authenticate": "Bearer"})

@route_calendar.get("/unidad")
def schedule(unidad: str, response = Depends(decode_token)):
    if response:
        db_unidad = session.query(Schedules).where(Schedules.unidad == unidad).all() 

        if db_unidad:
            return db_unidad[0]
        
        return False    
    
    raise http_error(401, "Token Invalido") 

@route_calendar.get("/unidades")
def schedules(response = Depends(decode_token)):
    if response:
        db_unidad = session.query(Schedules).all()          
        return db_unidad       
   
    raise http_error(401, "Token Invalido")
