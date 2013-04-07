"""Main entry point
"""
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

db_url = "sqlite:////tmp/test.db"


def main(global_config, **settings):
    # Session factory
    session_factory = UnencryptedCookieSessionFactoryConfig(
            settings['session.secret'])

    # Configurator setup
    config = Configurator(settings=settings,
                          session_factory=session_factory)
    config.scan("panstora.views")

    # Static view setup
    if settings.get('url_prefix', None):
        config.add_static_view('http://%s/static' % settings['url_prefix'],
                               'panstora:static')
    else:
        config.add_static_view('static', 'static', cache_max_age=3600)

    # Set up routes
    config.add_route('index', '/')
    config.add_route('item', '/item/{item_code}')
    config.add_route('cart', '/cart')
    config.add_route('cart_add', '/cart/add')
    config.add_route('error', '/error')

    db_url = settings['database.url']

    return config.make_wsgi_app()
