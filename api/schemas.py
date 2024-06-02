from pydantic import BaseModel
from typing import Optional
from datetime import date


class DepartamentoBase(BaseModel):
    piso: Optional[str] = None
    precio: Optional[float] = None
    garantia: Optional[float] = None

    class Config:
        orm_mode: True


class DepartamentoCreate(DepartamentoBase):
    pass


class DepartamentoUpdate(DepartamentoBase):
    pass


class DepartamentoInDBBase(DepartamentoBase):
    id_departamento: int


class InquilinoBase(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    cedula: Optional[str] = None

    class Config:
        orm_mode: True


class InquilinoCreate(InquilinoBase):
    pass


class InquilinoUpdate(InquilinoBase):
    pass


class InquilinoInDBBase(InquilinoBase):
    id_inquilino: int


class ArriendoBase(BaseModel):
    id_inquilino: int
    id_departamento: int

    fecha_inicio: date

    class Config:
        orm_mode: True


class ArriendoCreate(ArriendoBase):
    pass


class ArriendoUpdate(ArriendoBase):
    pass


class ArriendoInDBBase(ArriendoBase):
    id_arriendo: int
    dia_corte: int


class ArriendoJoin(BaseModel):
    fecha_inicio: date
    dia_corte: int
    inquilino: InquilinoInDBBase
    departamento: DepartamentoInDBBase
