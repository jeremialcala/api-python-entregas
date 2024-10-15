from sqlalchemy import create_engine, Column, Integer, String, DATE, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .entity_base import Base

engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')

Base.metadata.create_all(engine)


class EntregaEmplado(Base):
    __tablename__='entrega_a_empleados'
    id_beneficio = Column(Integer, ForeignKey("beneficios.id_beneficio"), primary_key=True)
    id_empleado = Column(Integer, ForeignKey("empleado.id_empleado"), primary_key=True)
    id_unidad_org = Column(Integer, ForeignKey("unidad_org.id_unidad_org"), primary_key=True)
    id_codnom = Column(Integer, ForeignKey("nomina.id_codnom"), primary_key=True)
