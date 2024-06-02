from sqlalchemy.orm import Session
from . import models as md
from . import schemas as sch


def create_inquilino(db: Session, inq: sch.InquilinoCreate):
    to_create = md.Inquilino(
        nombre=inq.nombre, apellido=inq.apellido, cedula=inq.cedula
    )

    db.add(to_create)
    db.commit()
    db.refresh(to_create)

    return to_create


def create_departamento(db: Session, dep: sch.DepartamentoCreate):
    to_create = md.Departamento(piso=dep.piso, precio=dep.precio, garantia=dep.garantia)

    db.add(to_create)
    db.commit()
    db.refresh(to_create)

    return to_create


def create_arriendo(db: Session, ar: sch.ArriendoCreate):
    to_create = md.Arriendo(
        id_inquilino=ar.id_inquilino,
        id_departamento=ar.id_departamento,
        fecha_inicio=ar.fecha_inicio,
    )

    db.add(to_create)
    db.commit()
    db.refresh(to_create)

    return to_create


def get_inquilino_cedula(db: Session, ced: str):
    return db.query(md.Inquilino).filter(md.Inquilino.cedula == ced).first()


def get_inquilino_id(db: Session, id_inq: int):
    return db.query(md.Inquilino).filter(md.Inquilino.id_inquilino == id_inq).first()


""" def get_arriendo_id(db: Session, id_ar: int):
    return db.query(md.Arriendo).filter(md.Arriendo.id_arriendo == id_ar).first() """


def get_arriendo_id(db: Session, id_ar: int):
    return (
        db.query(md.Arriendo)
        .join(md.Inquilino, md.Arriendo.id_inquilino == md.Inquilino.id_inquilino)
        .join(
            md.Departamento,
            md.Arriendo.id_departamento == md.Departamento.id_departamento,
        )
        .filter(md.Arriendo.id_arriendo == id_ar)
        .first()
    )


def get_arriendo_piso(db: Session, piso_dep: str):
    return (
        db.query(md.Arriendo)
        .join(md.Inquilino, md.Arriendo.id_inquilino == md.Inquilino.id_inquilino)
        .join(
            md.Departamento,
            md.Arriendo.id_departamento == md.Departamento.id_departamento,
        )
        .filter(md.Departamento.piso == piso_dep)
        .first()
    )


def get_departamento_id(db: Session, id_dep: int):
    return (
        db.query(md.Departamento)
        .filter(md.Departamento.id_departamento == id_dep)
        .first()
    )
