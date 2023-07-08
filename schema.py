from pydantic import BaseModel
from typing import List, Dict

class Login(BaseModel):
    username: str
    password: str

class User(Login):
    name: str     
    
class Person(BaseModel):    
    dni: str
    paterno: str
    materno: str
    nombre: str
    nacimiento: str
    ingreso: str   
    cargo: str  

class Apoyo(BaseModel):
    dia: int
    nombre: str
    turno: str

class Turno(BaseModel):
    dia: List[int]
    noche: List[int]

class Calendar(BaseModel):    
    unidad: str
    trabajadores: List[str]
    turnos: Turno
    apoyos: List[Apoyo]

    