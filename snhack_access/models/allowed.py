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
    ForeignKey,
#    Text,
    )
from sqlalchemy.orm import relationship, backref

class Allowed(Base):
    __tablename__ = 'allowed'
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    accessible_thing_id = Column(Integer, ForeignKey('accessible_things.id'),  primary_key=True)
    is_admin = Column(Boolean)

    person = relationship('Person', backref=backref('allowed', order_by='Person.id'))
    accessible_thing = relationship('AccessibleThing', backref=backref('allowed', order_by='AccessibleThing.id'))
