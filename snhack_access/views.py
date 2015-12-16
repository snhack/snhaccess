from pyramid.view import view_config

from .models.meta import (
    DBSession,
)
from .models import (
    Person,
)

@view_config(route_name='list_members',
             renderer='json',
             request_method='GET')
def list_members(request):
    people = DBSession.query(Person).all()
    for person in people:
        print person.__dict__
    people_list = [ p.__dict__ for p in people ]


    
