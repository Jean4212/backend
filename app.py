from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import Users, Persons, Calendars, session
from schema import User, Person, Login, Calendar
from typing import List

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")   
def index():  

    q = session.query(Calendars).all()

    if q:
        for item in q:
            myDict = {"unidad": item.unidad,
                      "trabajadores": item.trabajadores,
                      "turnos": item.turnos,
                      "apoyos": item.apoyos}
            print(myDict)    
   
    return myDict

@app.get("/users")
def get_users():
    
    users = session.query(Users).all()   
    myArray = []

    if users:     
        for user in users:
            myArray.append(user)

    return myArray   

@app.post("/users")
def post_users(users: List[User]):
    
    new_users = [Users(name=u.name, username=u.username, password=u.password) for u in users]
    session.add_all(new_users)
    session.commit()      
   
    return True

@app.delete("/users")
def delete_users():
    
    session.execute(Users.__table__.delete())
    session.commit()
   
    return True

@app.get("/persons")
def get_persons():

    persons = session.query(Persons).all() 
    myArray = []

    if persons:
        for person in persons:
            myArray.append(person)

    return myArray   

@app.post("/persons")
def post_persons(persons: List[Person]):
   
    new_persons = [Persons(dni=p.dni, paterno=p.paterno, materno=p.materno, nombre=p.nombre, nacimiento=p.nacimiento, 
                           ingreso=p.ingreso, cargo=p.cargo) for p in persons]    
    session.add_all(new_persons)
    session.commit()      
   
    return True

@app.delete("/persons")
def delete_persons():
        
    session.execute(Persons.__table__.delete())
    session.commit()
   
    return True

@app.get("/calendars")
def get_calendars():

    calendars = session.query(Calendars).all() 
    myArray = []

    if calendars:
        for calendar in calendars:
            myArray.append(calendar)

    return myArray   

@app.post("/calendars")
def post_calendars(calendar: List[Calendar]):
  
    new_calendars = []   

    for c in calendar:
        new_calendar = c.json().

        #new_calendars.append[new_calendar]      
    
    #session.add_all(new_calendars)  
    #session.commit()      
   
    return True

@app.post("/login")
def post_calendars(user: Login):
   
    users = session.query(Users).filter(Users.username == user.username).all()

    if users:        
        u = users[0] 
           
        if u.password == user.password:   
            return {"username": u.username, "name": u.name}
    
    return False