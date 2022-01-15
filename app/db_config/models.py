from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Uuid(Base):
    __tablename__ = "uuid"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    createdAt = Column(String)

