from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import schemas as sch
from . import crud as cr
from .functions import validate as va

from .database import get_db

app = FastAPI(title="Comtex765", version="1.0.0")


@app.get("/")
def read_root():
    return {"Saludo": "Hola a todos"}


@app.post("/inquilino/")
def create_inquilino(schema: sch.InquilinoBase, db: Session = Depends(get_db)):
    db_inquilino = cr.get_inquilino_cedula(db, ced=schema.cedula)

    if db_inquilino:
        raise HTTPException(status_code=400, detail="Inquilino already registered")

    if not va.validate_cedula(schema.cedula):
        raise HTTPException(status_code=400, detail="Cedula is not valid")

    created = cr.create_inquilino(db=db, inq=schema)

    return {"Success": True, "Id nuevo inquilino": created.id_inquilino}


@app.post("/departamento/")
def create_departamento(schema: sch.DepartamentoBase, db: Session = Depends(get_db)):
    created = cr.create_departamento(db=db, dep=schema)

    return {"Success": True, "ID": created.id_departamento, "Precio": created.precio}


@app.post("/arriendo/")
def create_arriendo(schema: sch.ArriendoBase, db: Session = Depends(get_db)):
    created = cr.create_arriendo(db=db, ar=schema)

    return {
        "Success": True,
        "ID arrieendo": created.id_arriendo,
        "Día de corte": created.dia_corte,
    }


@app.get("/inquilinos/", response_model=list[sch.InquilinoInDBBase])
def inquilinos(db: Session = Depends(get_db)):
    return cr.get_all_inquilinos(db)


@app.get("/arriendos/", response_model=list[sch.ArriendoInDBBase])
def arriendos(db: Session = Depends(get_db)):
    return cr.get_all_arriendos(db)


@app.get("/departamentos/", response_model=list[sch.DepartamentoInDBBase])
def departamentos(db: Session = Depends(get_db)):
    return cr.get_all_departamentos(db)


@app.get("/inquilino/cedula/{cedula}", response_model=sch.InquilinoInDBBase)
def inquilino_by_id(cedula: str, db: Session = Depends(get_db)):
    db_inquilino = cr.get_inquilino_cedula(db=db, ced=cedula)
    if db_inquilino is None:
        raise HTTPException(status_code=404, detail="Inquilino not found")
    return db_inquilino


@app.get("/inquilino/id/{id}", response_model=sch.InquilinoInDBBase)
def inquilino_by_id(id: int, db: Session = Depends(get_db)):
    db_inquilino = cr.get_inquilino_id(db=db, id_inq=id)
    if db_inquilino is None:
        raise HTTPException(status_code=404, detail="Inquilino not found")
    return db_inquilino


""" @app.get("/arriendo/id/{id}", response_model=sch.ArriendoInDBBase)
def arriendo_by_id(id: int, db: Session = Depends(get_db)):
    db_arriendo = cr.get_arriendo_id(db=db, id_ar=id)
    if db_arriendo is None:
        raise HTTPException(status_code=404, detail="Arriendo not found")
    return db_arriendo """


@app.get("/arriendo/id/{id}", response_model=sch.ArriendoJoin)
def arriendo_by_id(id: int, db: Session = Depends(get_db)):
    db_arriendo = cr.get_arriendo_id(db=db, id_ar=id)
    if db_arriendo is None:
        raise HTTPException(status_code=404, detail="Arriendo not found")
    return db_arriendo


@app.get("/arriendo/piso/{piso}", response_model=sch.ArriendoJoin)
def arriendo_by_piso(piso: str, db: Session = Depends(get_db)):
    db_arriendo = cr.get_arriendo_piso(db=db, piso_dep=piso)
    if db_arriendo is None:
        raise HTTPException(status_code=404, detail="Arriendo not found")
    return db_arriendo


@app.get("/departamento/id/{id}", response_model=sch.DepartamentoInDBBase)
def departamento_by_id(id: int, db: Session = Depends(get_db)):
    db_departamento = cr.get_departamento_id(db=db, id_dep=id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento not found")
    return db_departamento


@app.put("/inquilino/{id}", response_model=sch.InquilinoUpdate)
def update_inquilino(
    id: int, schema: sch.InquilinoUpdate, db: Session = Depends(get_db)
):
    db_inquilino = cr.get_inquilino_id(db=db, id_inq=id)
    if db_inquilino is None:
        raise HTTPException(status_code=404, detail="Inquilino not found")

    success = cr.update_inquilino(
        db=db, id_inq=db_inquilino.id_inquilino, update_data=schema
    )

    if success is None:
        raise HTTPException(status_code=404, detail="Inquilino not updated")
    return success


@app.put("/departamento/{id}", response_model=sch.DepartamentoUpdate)
def update_departamento(
    id: int, schema: sch.DepartamentoUpdate, db: Session = Depends(get_db)
):
    db_departamento = cr.get_departamento_id(db=db, id_dep=id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento not found")

    success = cr.update_departamento(
        db=db, id_dep=db_departamento.id_departamento, update_data=schema
    )

    if success is None:
        raise HTTPException(status_code=404, detail="Departamento not updated")
    return success


@app.put("/arriendo/{id}", response_model=sch.ArriendoUpdate)
def update_arriendo(id: int, schema: sch.ArriendoUpdate, db: Session = Depends(get_db)):
    db_arriendo = cr.get_arriendo_id(db=db, id_ar=id)
    if db_arriendo is None:
        raise HTTPException(status_code=404, detail="Arriendo not found")

    success = cr.update_arriendo(
        db=db, id_ar=db_arriendo.id_arriendo, update_data=schema
    )

    if success is None:
        raise HTTPException(status_code=404, detail="Arriendo not updated")
    return success


@app.delete("/inquilino/{id}", response_model=sch.InquilinoInDBBase)
def delete_inquilino(id: int, db: Session = Depends(get_db)):
    db_inquilino = cr.get_inquilino_id(db=db, id_inq=id)
    if db_inquilino is None:
        raise HTTPException(status_code=404, detail="Inquilino not found")

    deleted_inquilino = cr.delete_inquilino(db=db, id_inq=id)
    return deleted_inquilino


@app.delete("/departamento/{id}", response_model=sch.DepartamentoInDBBase)
def delete_departamento(id: int, db: Session = Depends(get_db)):
    db_departamento = cr.get_departamento_id(db=db, id_dep=id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento not found")

    deleted_departamento = cr.delete_departamento(db=db, id_dep=id)
    return deleted_departamento


@app.delete("/arriendo/{id}", response_model=sch.ArriendoInDBBase)
def delete_arriendo(id: int, db: Session = Depends(get_db)):
    db_arriendo = cr.get_arriendo_id(db=db, id_ar=id)
    if db_arriendo is None:
        raise HTTPException(status_code=404, detail="Arriendo not found")

    deleted_arriendo = cr.delete_arriendo(db=db, id_ar=id)
    return deleted_arriendo
