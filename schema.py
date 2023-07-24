from pydantic import BaseModel
    
class User(BaseModel):
    username: str
    password: str
    name: str
    email: str
    active: bool = True

class Person(BaseModel):    
    dni: str
    paterno: str
    materno: str
    nombre: str
    nacimiento: str
    ingreso: str   
    cargo: str  

class Schedule(BaseModel):
    unidad: str
    trabajadores: list
    turno_dia: list
    turno_noche: list

    