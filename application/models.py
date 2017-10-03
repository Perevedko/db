from sqlalchemy import Column, Integer, String, DateTime, Float, UniqueConstraint
from db import Base


class Datapoint(Base):

    __tablename__ = 'datapoints'

    __table_args__ = (
        UniqueConstraint("freq", "name", "date"),
    )

    id = Column(Integer, nullable=False, 
                         unique=True, 
                         autoincrement=True,
                         primary_key=True)
    freq = Column(String, nullable=False)
    name = Column(String, nullable=False)
    date = Column(String, nullable=False)


    value = Column(Float, nullable=False)
