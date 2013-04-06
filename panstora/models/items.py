from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    relation,
    backref,
    column_property,
    synonym,
    joinedload,
)

from sqlalchemy.types import (
    Integer,
    Unicode,
)

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from zope.sqlalchemy import ZopeTransactionExtension

from pyramid.security import (
    Everyone,
    Authenticated,
    Allow,
)

from panstora.models import Base

from panstora.utils import (
    hash_password,
    encode58,
    decode58
)

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


tag_item_assoc_table = Table(
    'association', Base.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id_')),
    Column('item_id', Integer, ForeignKey('items.id_'))
)


class Item(Base):
    """
    An item from the store.
    """
    __tablename__ = 'items'
    id_ = Column(Integer, primary_key=True)
    name = Column(Unicode(50), unique=True, index=True)
    description = Column(Unicode(256), unique=True, index=True)
    tags = relationship('Tag', secondary=tag_item_assoc_table)

    def _get_code(self):
        return encode58(self.id_)

    def _set_code(self, newcode):
        raise NotImplementedError("You can't set this property.")

    code = property(_get_code, _set_code)
    code = synonym('_code', descriptor=code)

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_by_name(cls, name):
        it = DBSession.query(cls).filter(cls.name == name)
        return it.first()

    @classmethod
    def get_by_code(cls, code):
        it = DBSession.query(cls).filter(cls.code == code)
        return it.first()

class Tags(Base):
    __tablename__ = 'tags'
    id_ = Column(Integer, primary_key=True)
    name = Column(Unicode(50), unique=True, index=True)
    items = relationship('Item', secondary=tag_item_assoc_table)
