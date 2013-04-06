from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
)

from pyramid.view import view_config

from panstora.models import User, Item, Tag


@view_config(route_name='index', renderer='index.mak')
def index_view(request):
    return {}


@view_config(route_name='item', renderer='item.mak')
def item_view(request):
    item = Item.get_by_code(int(request.matchdict.get('item_code')))
    if item is None:
        # There's no item with that ID, so go back home for now
        return HTTPFound(location=request.route_url('index'))
    # Otherwise, let's return the item data to the item view
    return {
        'item': item,
    }
