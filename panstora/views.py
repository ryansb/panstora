from pyramid.view import view_config

@view_config(route_name='index', renderer='index.mak')
def home_view(request):
    return {}
