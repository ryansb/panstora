from pyramid.view import view_config

from panstora.models import User, Item, Tag


@view_config(route_name='index', renderer='index.mak')
def index_view(request):
    return {}


@view_config(route_name='item', renderer='item.mak')
def item_view(request):
    item_id = request.matchdict.get('item_id')
    item = Item.get_by_code(item_id)
    return {
        'item_id': item_id,
        'item_name': item.name,
    }
