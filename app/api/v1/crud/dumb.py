from .. import models
from .. import schemas
from sqlalchemy.orm import Session


def create_dumb(db: Session, dumb: schemas.DumbIn) -> models.Dumb:
    db_dumb = models.Dumb(string=dumb.string)
    db.add(db_dumb)
    db.commit()
    db.refresh(db_dumb)
    return db_dumb


def get_all_dumbs(db: Session) -> list[models.Dumb]:
    return db.query(models.Dumb).all()


def get_dumb_by_id(db: Session, dumb_id: int) -> models.Dumb | None:
    return db.query(models.Dumb).filter(models.Dumb.id == dumb_id).first()


def delete_dumb_by_id(db: Session, dumb_id: int) -> models.Dumb | None:
    db_dumb = db.query(models.Dumb).filter(models.Dumb.id == dumb_id).first()
    if db_dumb:
        db.delete(db_dumb)
        db.commit()
    return db_dumb
