from pyramid.view import view_config


@view_config(route_name='index', renderer='index.mak')
def index_view(request):
    return {}


@view_config(route_name='item', renderer='item.mak')
def item_view(request):
    item_id = request.matchdict.get('item_id')
    return {
        'item_id': item_id,
    }
