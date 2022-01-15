from sqlalchemy.orm import Session

from . import models, schemas


def get_uuid(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Uuid).offset(skip).limit(limit).all()


def create_uuid(db: Session, uuid: schemas.UuidCreate):
    db_uuid = models.Uuid(uuid=uuid.uuid,)
    db.add(db_uuid)
    db.commit()
    db.refresh(db_uuid)
    return db_uuid
