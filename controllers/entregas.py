# -*- coding: utf-8 -*-
import logging
import json
from fastapi import HTTPException, status, Request, Response
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from classes import APIResponse, EntregaEmplado, Empleado


async def ctr_entregar_beneficio(request: Request) -> Response:
    respuesta = APIResponse(codigo=200)
    engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')
    Session = sessionmaker(bind=engine)
    session = Session()
    req = await request.json()
    entrega = EntregaEmplado(**req)
    session.add(entrega)
    session.commit()
    return Response(status_code=respuesta.codigo, media_type="Application/json", content=respuesta.json())


async def ctr_obtener_entregas_por_beneficio(beneficios: list) -> Response:
    respuesta = APIResponse(codigo=200)
    engine = create_engine('mysql+pymysql://root:b380f76985b9@127.0.0.1:32306/beneficios')
    Session = sessionmaker(bind=engine)
    session = Session()
    # buscamos los empleados

    empleados = [jsonable_encoder(empleado.__dict__) for empleado in session.query(Empleado).all()]
    # (18, 19, 21);
    condicion = session.query(EntregaEmplado.id_beneficio).filter(
        EntregaEmplado.id_beneficio.in_([int(id_beneficio) for id_beneficio in beneficios])
    )

    data = [jsonable_encoder(entrega.__dict__) for entrega in session.query(EntregaEmplado).filter(
        EntregaEmplado.id_beneficio.in_(condicion))]

    lista_entrega = []

    for empleado in empleados:
        empleado["beneficios"] = [
            beneficio["id_beneficio"] for beneficio in
            list(filter(lambda x: x["id_empleado"] == empleado['id_empleado'], data))]
        lista_entrega.append(empleado)

    respuesta.data = lista_entrega
    return Response(status_code=respuesta.codigo, media_type="Application/json", content=respuesta.json())
