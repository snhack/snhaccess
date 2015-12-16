from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.meta import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('add_member', '/members/add')
    config.add_route('update_member', '/members/update')
    config.add_route('list_members', '/members/list')
    config.add_route('add_token', '/tokens/add')
    config.add_route('update_token', '/tokens/update')
    config.add_route('add_thing', '/things/add')
    config.add_route('add_access', '/access/add')
    config.add_route('revoke_access', '/access/revoke')
    config.add_route('check_access', '/access/check')
    config.scan()
    return config.make_wsgi_app()
