from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel


import uuid
import datetime

from ..db_config import crud, models, schemas
from ..db_config.database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/uuid/", tags=["uuid"], response_model=List[schemas.Uuid])
def read_uuids(uuid: schemas.UuidCreate, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    newUuid =  crud.create_uuid(db=db, uuidVal=uuid)
    uuids =   crud.get_uuid(db, skip=skip, limit=limit)
    return uuids
    # # Define an emp[ty list to hold data and dictionary to ho;ld each item
    # data = []
    # uuidDatum = {}
    # # generate uuid
    # newUuid = uuid.uuid1()
    # uuidDatum['uuid'] = newUuid
    # uuidDatum['createdAt'] = datetime.datetime.now()
    # data.append(uuidDatum)
    # print(newUuid)

    # return data

