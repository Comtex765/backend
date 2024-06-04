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


def get_all_inquilinos(db: Session):
    return db.query(md.Inquilino).all()


def get_inquilino_cedula(db: Session, ced: str):
    return db.query(md.Inquilino).filter(md.Inquilino.cedula == ced).first()


def get_inquilino_id(db: Session, id_inq: int):
    return db.query(md.Inquilino).filter(md.Inquilino.id_inquilino == id_inq).first()


""" def get_arriendo_id(db: Session, id_ar: int):
    return db.query(md.Arriendo).filter(md.Arriendo.id_arriendo == id_ar).first() """


def get_all_arriendos(db: Session):
    return db.query(md.Arriendo).all()


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


def get_all_departamentos(db: Session):
    return db.query(md.Departamento).all()


def get_departamento_id(db: Session, id_dep: int):
    return (
        db.query(md.Departamento)
        .filter(md.Departamento.id_departamento == id_dep)
        .first()
    )


def update_inquilino(db: Session, id_inq: int, update_data: sch.InquilinoUpdate):
    db_inquilino = (
        db.query(md.Inquilino).filter(md.Inquilino.id_inquilino == id_inq).first()
    )

    for field, value in update_data.model_dump(exclude_unset=True).items():
        if value != "":
            setattr(db_inquilino, field, value)

    db.commit()
    db.refresh(db_inquilino)

    return db.query(md.Inquilino).filter(md.Inquilino.id_inquilino == id_inq).first()


def update_departamento(db: Session, id_dep: int, update_data: sch.DepartamentoUpdate):
    db_departamento = (
        db.query(md.Departamento)
        .filter(md.Departamento.id_departamento == id_dep)
        .first()
    )

    for field, value in update_data.model_dump(exclude_unset=True).items():
        if value not in [None, "", 0]:
            setattr(db_departamento, field, value)

    db.commit()
    db.refresh(db_departamento)

    return (
        db.query(md.Departamento)
        .filter(md.Departamento.id_departamento == id_dep)
        .first()
    )


def update_arriendo(db: Session, id_ar: int, update_data: sch.ArriendoUpdate):
    db_arriendo = db.query(md.Arriendo).filter(md.Arriendo.id_arriendo == id_ar).first()

    for field, value in update_data.model_dump(exclude_unset=True).items():
        if value not in [None, "", 0]:
            setattr(db_arriendo, field, value)

    db.commit()
    db.refresh(db_arriendo)

    return db_arriendo


def delete_arriendo(db: Session, id_ar: int):
    db_arriendo = db.query(md.Arriendo).filter(md.Arriendo.id_arriendo == id_ar).first()
    db.query(md.Arriendo).filter(md.Arriendo.id_arriendo == id_ar).delete()
    db.commit()

    return db_arriendo


def delete_inquilino(db: Session, id_inq: int):
    db_inquilino = (
        db.query(md.Inquilino).filter(md.Inquilino.id_inquilino == id_inq).first()
    )
    db.query(md.Inquilino).filter(md.Inquilino.id_inquilino == id_inq).delete()
    db.commit()

    return db_inquilino


def delete_departamento(db: Session, id_dep: int):
    db_departamento = (
        db.query(md.Departamento)
        .filter(md.Departamento.id_departamento == id_dep)
        .first()
    )
    db.query(md.Departamento).filter(md.Departamento.id_departamento == id_dep).delete()
    db.commit()

    return db_departamento
