from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)

from sqlalchemy.orm import (
    relationship,
    relation,
    backref,
    column_property,
    synonym,
    joinedload,
)

from sqlalchemy.types import (
    Integer,
    Float,
    Unicode,
)

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from pyramid.security import (
    Everyone,
    Authenticated,
    Allow,
)

from panstora.models import Base, DBSession

cart_item_assoc_table = Table(
    'cart_item_assoc', Base.metadata,
    Column('cart', Integer, ForeignKey('carts.id_')),
    Column('item_id', Integer, ForeignKey('items.id_'))
)

class Cart(Base):
    __tablename__ = 'carts'
    id_ = Column(Integer, primary_key=True)
    items = relationship('Item', secondary=cart_item_assoc_table)
    owner_id = Column(Integer, ForeignKey('users.id_'))

    def put(self):
        DBSession.add(self)
        DBSession.flush()
