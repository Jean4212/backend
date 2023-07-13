from sqlalchemy import String, JSON, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from os import getcwd

# Conexion con Sqlite3
DATABASE_URL = f"sqlite:///{getcwd()}/db.db"
engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)    
    username: Mapped[str] = mapped_column(String(10))
    password: Mapped[str] = mapped_column(String(10))  
    name:  Mapped[str] = mapped_column(String(30))  
    email: Mapped[str] = mapped_column(String(30))
    active: Mapped[bool] = mapped_column(Boolean)  

    def __repr__(self) -> str:        
        return f"Users(id={self.id!r}, username={self.username!r}, password={self.password!r}, name={self.name!r}, email={self.email!r}, active={self.active!r})"

class Persons(Base):
    __tablename__ = "persons"
    id: Mapped[int] = mapped_column(primary_key=True)
    dni: Mapped[str] = mapped_column(String(8))
    paterno: Mapped[str] = mapped_column(String(20))
    materno: Mapped[str] = mapped_column(String(20))
    nombre: Mapped[str] = mapped_column(String(30))
    nacimiento: Mapped[str] = mapped_column(String(10))   
    ingreso: Mapped[str] = mapped_column(String(10))   
    cargo: Mapped[str] = mapped_column(String(30))        

    def __repr__(self) -> str:                
        return f"""Persons(id={self.id!r}, dni={self.dni!r}, paterno={self.paterno!r}, materno={self.materno!r}, nombre={self.nombre!r}, nacimiento={self.nacimiento!r}, ingreso={self.ingreso!r}, cargo={self.cargo!r})"""

class Calendars(Base):
    __tablename__ = 'calendars'
    id: Mapped[int] = mapped_column(primary_key=True)
    unidad: Mapped[str] = mapped_column(String)
    trabajadores: Mapped[list] = mapped_column(JSON)
    turnos: Mapped[list] = mapped_column(JSON)
    apoyos: Mapped[list] = mapped_column(JSON)

    def __repr__(self) -> str:                
        return f"""Calendars(id={self.id!r}, unidad={self.unidad!r}, trabajadores={self.trabajadores!r}, turnos={self.turnos!r}, apoyos={self.apoyos!r})"""

Base.metadata.create_all(engine)
session = Session(engine)