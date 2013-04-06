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

from panstora.utils import (
    hash_password,
    encode58,
    decode58
)


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
    description = Column(Unicode(256))
    tags = relationship('Tag', secondary=tag_item_assoc_table)
    price = Column(Float)
    rack = Column(Integer)
    dept = Column(Unicode(64))

    def _get_code(self):
        return encode58(self.id_)

    def _set_code(self, newcode):
        raise NotImplementedError("You can't set this property.")

    code = property(_get_code, _set_code)
    code = synonym('_code', descriptor=code)

    def __init__(self, name=None):
        if name: self.name = name

    @classmethod
    def get_by_name(cls, name):
        it = DBSession.query(cls).filter(cls.name == name)
        return it.first()

    @classmethod
    def get_by_code(cls, code):
        print "hello there"
        it = DBSession.query(cls).filter(cls.id_ == decode58(code))
        return it.first()

    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()

    @classmethod
    def get_by_code(cls, code):
        it = DBSession.query(cls).filter(cls.code == code)
        return it.first()

    def to_dict(self, deep=False):
        if deep:
            return dict(
                id_=self.id_,
                name=self.name,
                tags=[t.to_dict() for t in self.tags],
            )
        return dict(
            id_=self.id_,
            name=self.name,
            tags=[t.name() for t in self.tags],
        )

    def put(self):
        DBSession.add(self)
        DBSession.commit()

class Tag(Base):
    __tablename__ = 'tags'
    id_ = Column(Integer, primary_key=True)
    name = Column(Unicode(50), unique=True, index=True)
    items = relationship('Item', secondary=tag_item_assoc_table)

    @classmethod
    def get_by_name(cls, name):
        it = DBSession.query(cls).filter(cls.name == name)
        return it.first()

    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()

    def to_dict(self, deep=False):
        if deep:
            return dict(
                id_=self.id_,
                name=self.name,
                items=[i.to_dict() for i in self.items],
            )
        return dict(
            id_=self.id_,
            name=self.name,
            items=[i.name for i in self.items],
        )

    def put(self):
        DBSession.add(self)
        DBSession.commit()
