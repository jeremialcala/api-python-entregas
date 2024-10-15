from sqlalchemy import create_engine, Column, Integer, String, DATE, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .entity_base import Base

engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')

Base.metadata.create_all(engine)

class Empleado(Base):
    __tablename__='empleados'
    id_empleado = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    cedula = Column(Integer)
