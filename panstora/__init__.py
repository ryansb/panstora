"""Main entry point
"""
from pyramid.config import Configurator

db_url = "sqlite:////tmp/test.db"


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.scan("panstora.views")

    # Static view setup
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Set up routes
    config.add_route('index', '/')
    config.add_route('item', '/item/{item_id}')

    db_url = settings['database.url']

    return config.make_wsgi_app()
