import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
from sqlalchemy.orm.exc import MultipleResultsFound

from pyramid.scripts.common import parse_vars

from ..models.meta import (
    DBSession,
    Base,
    )
from ..models import (
    Person,
    AccessToken,
    Allowed,
    Dues,
    AccessibleThing
    )

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        all_allowed = DBSession.query(Allowed).all()
        if len(all_allowed) == 0:
            person = Person(name=u'Jess Robinson', email=u'castaway@desert-island.me.uk', is_member=True)
            thing = AccessibleThing(name=u'Access Database')
            DBSession.add(person)
            DBSession.add(thing)
            person = DBSession.query(Person).filter_by(email=u'castaway@desert-island.me.uk').one()
            thing = DBSession.query(AccessibleThing).filter_by(name=u'Access Database').one()
            allowed = Allowed(person_id = person.id, accessible_thing_id = thing.id, is_admin=True)
            DBSession.add(allowed)
