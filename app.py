import json
import logging.config
import time
from uuid import uuid4

from fastapi import FastAPI, Request, Response
from fastapi import status

from controllers import ctr_crear_beneficio, ctr_obtener_beneficios, ctr_obtener_beneficio, ctr_crear_empleado, \
    ctr_obtener_entregas_por_beneficio
from controllers.empleados import ctr_buscar_empleado_por_cedula, ctr_obtener_empleados

description = """
Esta es un API que maneja el ciclo de vida de los benefcios para el Sistema de control de Beneficios

## Beneficios 

* /beneficio:
* /empleados:
* /productos:



"""


app = FastAPI(
    title="SGB",
    description=description
)

@app.post("/beneficio")
async def crear_beneficio(request: Request):
    return await ctr_crear_beneficio(request)

@app.get("/beneficios")
async def obtener_beneficios():
    return await ctr_obtener_beneficios()

@app.get("/beneficio/{id_beneficio}")
async def buscar_beneficio(id_beneficio: int):
    return await ctr_obtener_beneficio(id_beneficio)

@app.put("/beneficio/{id_beneficio}")
async def modificar_beneficio(request: Request, id_beneficio: str):
    pass

@app.delete("/beneficio/{id_beneficio}")
async def eliminar_beneficio():
    pass

@app.post("/empleado")
async def crear_emplado(request: Request):
    return await ctr_crear_empleado(request)

@app.get("/empleados")
async def obtener_empleados():
    return await ctr_obtener_empleados()

@app.get("/empleado/{cedula}")
async def buscar_emplado_por_cedula(request: Request, cedula: int):
    return await ctr_buscar_empleado_por_cedula(cedula)

@app.get("/entregas")
async def obtener_entregas_pendientes(request: Request):
    return await ctr_obtener_entregas_por_beneficio(request.query_params.get("id_beneficios").split(","))
