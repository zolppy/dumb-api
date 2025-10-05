from typing import List
from sqlalchemy.orm import Session
from .. import crud, schemas, database
from fastapi import APIRouter, Depends, HTTPException

dumb_router = APIRouter()


@dumb_router.post(path="/", response_model=schemas.DumbCreate)
def post_dumb(
    dumb: schemas.DumbIn, db: Session = Depends(database.get_db)
) -> schemas.DumbCreate:
    return crud.create_dumb(db=db, dumb=dumb)


@dumb_router.get(path="/", response_model=List[schemas.DumbCreate])
def get_all_dumbs(db: Session = Depends(database.get_db)) -> List[schemas.DumbCreate]:
    return crud.get_all_dumbs(db=db)


@dumb_router.get(path="/{dumb_id}", response_model=schemas.DumbCreate)
def get_dumb_by_id(dumb_id: int, db: Session = Depends(database.get_db)):
    db_dumb = crud.get_dumb_by_id(db, dumb_id=dumb_id)
    if db_dumb is None:
        raise HTTPException(status_code=404, detail="Dumb not found")
    return db_dumb


@dumb_router.delete(path="/{dumb_id}", response_model=schemas.DumbCreate)
def delete_dumb_by_id(dumb_id: int, db: Session = Depends(database.get_db)):
    db_dumb = crud.delete_dumb_by_id(db, dumb_id=dumb_id)
    if db_dumb is None:
        raise HTTPException(status_code=404, detail="Dumb not found")
    return db_dumb
