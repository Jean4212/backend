from fastapi import APIRouter, HTTPException
from model import Users, Persons, Schedules, session
from schema import User, Person, Schedule
from create_token import hash_password, verify_password

route_admin = APIRouter(tags=["admin"], responses={404: {"detail": "No encontrado"}})

def http_error(code: int, message: str):
    return HTTPException(status_code=code, detail=message, headers={"WWW-Authenticate": "Bearer"})

@route_admin.post("/crear-admin")
def add_admin(password: str):
    if password == "jean":
        db_admin = session.query(Users).where(Users.username == "admin").all()     
        if not db_admin:                 
            new_admin = Users(username="admin", password=hash_password("jean"), name="administrador", email="administrador@administrador.com", active=True)
            session.add(new_admin)
            session.commit()   

        return {"message": "Registrado correctamente"}  
    raise http_error(400, "Contraseña invalida")  

@route_admin.post("/crear-usuario")
def add_user(user: User, password: str):    
    admin = session.query(Users).where(Users.username == "admin").all()
    if admin:
        if verify_password(password, admin[0].password):
            db_user = session.query(Users).where(Users.username == user.username).all()
            if db_user:
                raise http_error(400, "Usuario registrado")
        
            new_user = Users(username=user.username, password=hash_password(user.password), name=user.name, email=user.email, active=user.active)
            session.add(new_user)
            session.commit()   
   
            return {"message": "Registrado correctamente"}  
        raise http_error(400, "Contraseña invalida")
    raise http_error(400, "Administrador no existe")

@route_admin.post("/crear-empleado")
def add_employee(person: Person, password: str): 
    admin = session.query(Users).where(Users.username == "admin").all()
    if admin:
        if verify_password(password, admin[0].password):
            db_person = session.query(Persons).where(Persons.dni == person.dni).all()
            if db_person:
                raise http_error(400, "Empleado registrado")
            
            new_person = Persons(dni=person.dni, paterno=person.paterno, materno=person.materno, nombre=person.nombre, nacimiento=person.nacimiento, ingreso=person.ingreso, cargo=person.cargo)
            session.add(new_person)
            session.commit()     
    
            return {"message": "Registrado correctamente"} 
        raise http_error(400, "Contraseña invalida")
    raise http_error(400, "Administrador no existe")

@route_admin.post("/crear-horario")
def add_calendar(calendar: Schedule, password: str): 
    admin = session.query(Users).where(Users.username == "admin").all()
    if admin:
        if verify_password(password, admin[0].password):
            db_calendar = session.query(Schedules).where(Schedules.unidad == calendar.unidad).all()
            if db_calendar:
                raise http_error(400, "Unidad registrada")
            
            new_calendar = Schedules(unidad=calendar.unidad, trabajadores=calendar.trabajadores, turno_dia=calendar.turno_dia, turno_noche=calendar.turno_noche)
            session.add(new_calendar)
            session.commit()     
    
            return {"message": "Registrado correctamente"} 
        raise http_error(400, "Contraseña invalida")
    raise http_error(400, "Administrador no existe")

@route_admin.post("/eliminar-todo")
def delete_all(password: str):
    admin = session.query(Users).where(Users.username == "admin").all()
    if admin:
        if verify_password(password, admin[0].password):
            session.execute(Users.__table__.delete())
            session.execute(Persons.__table__.delete())
            session.execute(Schedules.__table__.delete())
            session.commit()
            return {"message": "Se limpio las tablas"} 
        raise http_error(400, "Contraseña invalida")
    raise http_error(400, "Administrador no existe")