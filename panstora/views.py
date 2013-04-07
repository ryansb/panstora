import transaction

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
)

from pyramid.view import view_config

from panstora.models import Cart, Item, Tag, User


@view_config(route_name='index', renderer='index.mak')
def index_view(request):
    return {}


@view_config(route_name='item', renderer='item.mak')
def item_view(request):
    item = Item.get_by_code(int(request.matchdict.get('item_code')))
    if item is None:
        # There's no item with that ID, so go back home for now
        return HTTPFound(location=request.route_url('index'))
    dev_id = None
    user = None
    if request.GET:
        dev_id = request.GET['DEV_ID']
        user = User.get_by_dev_id(dev_id)
        # Store the dev_id for use in cart views
        request.session['dev_id'] = dev_id
        # Store the item code in case the user tries to add it to cart
        request.session['item_code'] = item.code
        # Store the user
        request.session['user'] = user
    return {
        'item': item,
        'dev_id': dev_id,
        'user': user,
    }


@view_config(route_name='cart', renderer='cart.mak')
def cart_view(request):
    try:
        dev_id = request.session['dev_id']
    except KeyError:
        return HTTPFound(location=request.route_url('error',
                error_msg="Could not find device ID. Try scanning an item."))
    user = User.get_by_dev_id(dev_id)
    return {
        'dev_id': dev_id,
        'user': user,
        'user_cart_items': user.cart.items,
    }


@view_config(route_name='cart_add')
def cart_add_view(request):
    # can't be passing around User and Item because of their
    # ORM nature... passing and using these objects will
    # result in a DetachedInstanceError, because the object
    # is not bound to a session properly, lazy load
    # operation of the cart attribute or whatever will not work.
    # So we have to do things this way
    user = User.get_by_dev_id(request.session['dev_id'])
    item_code = request.session['item_code']
    # The user may not have a cart. Let's hook them up.
    if not user.cart:
        user.cart = Cart()
    user.cart.items.append(Item.get_by_code(int(item_code)))
    user.put()
    transaction.commit()
    return HTTPFound(location=request.route_url('cart'))


@view_config(route_name='error', renderer='error.mak')
def error_view(request):
    try:
        error_msg = request.matchdict.get('error_msg')
    except KeyError:
        error_msg = "There wasn't an error! Move along..."
    return dict(error_msg=error_msg)
