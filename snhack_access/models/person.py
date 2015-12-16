import datetime
from snhack_access.models.meta import Base
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
    Boolean,
    Sequence,
#    Text,
    )
from sqlalchemy.orm import relationship, backref

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, Sequence('people_id_seq'), primary_key=True)
    name = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    is_member = Column(Boolean, default=False)
    createddate = Column(DateTime, default=datetime.datetime.utcnow)
    endate = Column(DateTime, nullable=True)

