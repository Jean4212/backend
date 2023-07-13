from fastapi import APIRouter, HTTPException, Depends
from model import Persons, session
from create_token import decode_token

get_persons = APIRouter(prefix="/persons", tags=["persons"], responses={404: {"detail": "No encontrado"}})

@get_persons.get("/")
def Get_persons(response = Depends(decode_token)):
    if response:
        persons = session.query(Persons).all()  
        return persons   
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})  
    raise error
    
