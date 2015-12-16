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

class Dues(Base):
    __tablename__ = 'dues'
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    for_month = Column(Integer, nullable = False, primary_key=True)
    is_paid = Column(Boolean, default=False)
    paid_on_date = Column(DateTime, nullable=True)
    amount = Column(Integer)

    person = relationship('Person', backref=backref('dues', order_by='Person.id'))

