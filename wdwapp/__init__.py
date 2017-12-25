__version__ = '0.0.4'

def main(global_config, **settings):

    from pyramid.config import Configurator
    from sqlalchemy import engine_from_config
    from pyramid.session import SignedCookieSessionFactory
    from .models import DBSession, Base

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    my_session_factory = SignedCookieSessionFactory(
        settings['session.secret'])

    config = Configurator(settings=settings,
                    session_factory=my_session_factory,
                    root_factory='wdwapp.models.Root')

    config.include('pyramid_chameleon')

    # Route for cron servvice
    config.add_route('service_get', '/cron')

    # Routes for web site
    config.add_route('wiki_view', '/')
    config.add_route('wikipage_add', '/add')
    config.add_route('wikipage_view', '/{uid}')
    config.add_route('wikipage_edit', '/{uid}/edit')

    # Static things
    config.add_static_view('deform_static', 'deform:static/')

    # Let's go
    config.scan('.views')
    config.scan('.services')
    return config.make_wsgi_app()
