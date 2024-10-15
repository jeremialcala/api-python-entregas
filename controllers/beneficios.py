# -*- coding: utf-8 -*-
import logging
import json
from fastapi import HTTPException, status, Request, Response
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from classes import Beneficio, APIResponse


async def ctr_crear_beneficio(request: Request) -> Response:
    respuesta = APIResponse(codigo=200)
    engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')
    Session = sessionmaker(bind=engine)
    session = Session()
    req = await request.json()
    beneficio = Beneficio(**req)
    session.add(beneficio)
    session.commit()
    return Response(status_code=respuesta.codigo, media_type="Application/json", content=respuesta.json())


async def ctr_obtener_beneficios()-> Response:
    respuesta = APIResponse(codigo=200)
    engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')
    Session = sessionmaker(bind=engine)
    session = Session()
    beneficios = session.query(Beneficio).filter_by(estatus='N').all()
    respuesta.data = [jsonable_encoder(beneficio.__dict__) for beneficio in beneficios]
    return Response(status_code=respuesta.codigo, media_type="Application/json", content=respuesta.json())


async def ctr_obtener_beneficio(id_beneficio: int) -> Response:
    respuesta = APIResponse(codigo=200)
    engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')
    Session = sessionmaker(bind=engine)
    session = Session()
    beneficio = session.query(Beneficio).filter_by(id_beneficio=id_beneficio).first()

    if type(beneficio) == Beneficio:
        respuesta.data = jsonable_encoder(beneficio)
    else:
        respuesta.codigo= 404
        respuesta.data = {}
        respuesta.mensaje = "Beneficio no encontrado"

    return Response(status_code=respuesta.codigo, media_type="Application/json", content=respuesta.json())


