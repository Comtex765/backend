from pydantic import BaseModel
from typing import Optional
from datetime import date


class DepartamentoBase(BaseModel):
    piso: str
    precio: float
    garantia: float

    class Config:
        orm_mode: True


class DepartamentoCreate(DepartamentoBase):
    pass


class DepartamentoUpdate(DepartamentoBase):
    piso: Optional[str] = ""
    precio: Optional[float] = 0
    garantia: Optional[float] = 0


class DepartamentoInDBBase(DepartamentoBase):
    id_departamento: int


class InquilinoBase(BaseModel):
    nombre: str
    apellido: str
    cedula: str

    class Config:
        orm_mode: True


class InquilinoCreate(InquilinoBase):
    pass


class InquilinoUpdate(BaseModel):
    nombre: Optional[str] = ""
    apellido: Optional[str] = ""
    cedula: Optional[str] = ""


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


class ArriendoUpdate(BaseModel):
    id_inquilino: Optional[int] = None
    id_departamento: Optional[int] = None
    fecha_inicio: Optional[date] = None


class ArriendoInDBBase(ArriendoBase):
    id_arriendo: int
    dia_corte: int


class ArriendoJoin(BaseModel):
    fecha_inicio: date
    dia_corte: int
    inquilino: InquilinoInDBBase
    departamento: DepartamentoInDBBase
