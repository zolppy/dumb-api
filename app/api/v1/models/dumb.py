from ..database import Base
from sqlalchemy import Column, Integer, String


class Dumb(Base):
    __tablename__ = "dumbs"

    id = Column(Integer, primary_key=True, index=True)
    string = Column(String, index=True)
