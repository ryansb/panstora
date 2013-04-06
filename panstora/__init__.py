"""Main entry point
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.scan("panstora.views")

    # Static view setup
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Set up routes
    config.add_route('home', '/')

    return config.make_wsgi_app()
