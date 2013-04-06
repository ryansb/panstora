""" Cornice services.
"""
from cornice import Service

from panstora.models import User


hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

users = Service('users', path='/users', description="Provides user info")

@users.get()
def get_users(request):
    return [u.to_dict() for u in User.all()]
