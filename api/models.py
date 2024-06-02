from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship
from .database import Base


class Departamento(Base):
    __tablename__ = "departamento"

    id_departamento = Column(
        "id_departamento", Integer, primary_key=True, autoincrement=True
    )
    piso = Column("piso", String(25))
    precio = Column("precio", DECIMAL(5, 2))
    garantia = Column("garantia", DECIMAL(5, 2))

    # Relationship with Arriendo
    arriendos = relationship("Arriendo", back_populates="departamento")


class Inquilino(Base):
    __tablename__ = "inquilino"

    id_inquilino = Column("id_inquilino", Integer, primary_key=True, autoincrement=True)
    nombre = Column("nombre", String(50))
    apellido = Column("apellido", String(50))
    cedula = Column("cedula", String(10), unique=True)

    # Relationship with Arriendo
    arriendos = relationship("Arriendo", back_populates="inquilino")


class Arriendo(Base):
    __tablename__ = "arriendo"

    id_arriendo = Column("id_arriendo", Integer, primary_key=True, autoincrement=True)

    id_inquilino = Column("id_inquilino", Integer, ForeignKey("inquilino.id_inquilino"))
    id_departamento = Column(
        "id_departamento", Integer, ForeignKey("departamento.id_departamento")
    )
    fecha_inicio = Column("fecha_inicio", Date)
    dia_corte = Column("dia_corte", Integer)

    # Relationships
    inquilino = relationship("Inquilino", back_populates="arriendos")
    departamento = relationship("Departamento", back_populates="arriendos")
