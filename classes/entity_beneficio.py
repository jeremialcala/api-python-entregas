from sqlalchemy import create_engine, Column, Integer, String, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .entity_base import Base

engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')

Base.metadata.create_all(engine)


class Beneficio(Base):
    __tablename__="beneficios"
    id_beneficio = Column(Integer, primary_key=True, autoincrement=True)
    fecha_entrega = Column(DATE)
    id_tipo_beneficio = Column(Integer)
    estatus = Column(Integer)

