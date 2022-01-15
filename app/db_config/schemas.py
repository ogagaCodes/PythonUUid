from typing import List, Optional

from pydantic import BaseModel


class UuidBase(BaseModel):
    uuidVal: str
    createdAt: str


class UuidCreate(UuidBase):
    uuidVal: str
    createdAt: str


class Uuid(UuidBase):
    id: int

    class Config:
        orm_mode = True
