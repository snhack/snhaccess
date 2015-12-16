import datetime
from snhack_access.models.meta import Base
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
    ForeignKey,
    Sequence,
#    Text,
    )

from sqlalchemy.orm import relationship, backref

class AccessibleThing(Base):
    __tablename__ = 'accessible_things'
    id = Column(Integer, Sequence('accessible_thing_id_seq'), primary_key=True)
    name = Column(Unicode(255), nullable=False, unique=True)

