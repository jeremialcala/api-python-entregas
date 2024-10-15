# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field
from faker import Faker

fk = Faker()


class APIResponse(BaseModel):
    codigo: int = Field(default=200, examples=[201, 204, 400, 401, 403])
    mensaje: str = Field(default="PROCESS COMPLETED SUCCESSFULLY")
    data: list | dict = None
    timestamp: datetime = datetime.now()

