import datetime
from snhack_access.models.meta import Base
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Unicode,
    UnicodeText,
    DateTime,
    ForeignKey,
#    Text,
    )
from sqlalchemy.orm import relationship, backref

class AccessToken(Base):
    __tablename__ = 'access_tokens'
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    id = Column(String(255))
    type = Column(String(20), primary_key=True)

    person = relationship('Person', backref=backref('access_tokens', order_by='Person.id'))
