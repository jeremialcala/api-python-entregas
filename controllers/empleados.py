# -*- coding: utf-8 -*-
import logging
import json
from fastapi import HTTPException, status, Request, Response
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from classes import APIResponse, Empleado


async def ctr_crear_empleado(request: Request) -> Response:
    respuesta = APIResponse(code=200)
    empleado = Empleado(**await request.json())
    engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(empleado)
    session.commit()
    return Response(status_code=respuesta.codigo, media_type="Application/json", content=respuesta.json())


async def ctr_buscar_empleado_por_cedula(cedula: int)-> Response:
    respuesta = APIResponse(codigo=200)
    engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')
    Session = sessionmaker(bind=engine)
    session = Session()
    empleado = session.query(Empleado).filter_by(cedula=cedula).first()
    if type(empleado) == Empleado:
        respuesta.data = jsonable_encoder(empleado)
    else:
        respuesta.codigo= 404
        respuesta.data = {}
        respuesta.mensaje = "Empleado no encontrado"

    return Response(status_code=respuesta.codigo, media_type="Application/json", content=respuesta.json())


async def ctr_obtener_empleados() -> Response:
    respuesta = APIResponse(codigo=200)
    engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')
    Session = sessionmaker(bind=engine)
    session = Session()
    empleados = session.query(Empleado).all()
    respuesta.data = [jsonable_encoder(empleado.__dict__) for empleado in empleados]

    return Response(status_code=respuesta.codigo, media_type="Application/json", content=respuesta.json())


