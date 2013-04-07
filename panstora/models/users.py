import cryptacular.bcrypt

from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)

from sqlalchemy.orm import (
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


crypt = cryptacular.bcrypt.BCRYPTPasswordManager()


class User(Base):
    """
    Application's user model.
    """
    __tablename__ = 'users'
    id_ = Column(Integer, primary_key=True)
    username = Column(Unicode(32), unique=True)
    name = Column(Unicode(64))
    email = Column(Unicode(64))
    dev_id = Column(Unicode(64), unique=True)
    cart = relation('Cart', uselist=False, backref='owner')

    _password = Column('password', Unicode(64))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, dev_id, username=None, password=None, name=None, email=None):
        self.dev_id = dev_id
        if username: self.username = username
        if name: self.name = name
        if email: self.email = email
        if password: self.password = password

    def to_dict(self):
        return dict(
            username=self.username,
            name=self.name,
            email=self.email,
        )

    @classmethod
    def get_by_username(cls, username):
        return DBSession.query(cls).filter(cls.username == username).first()

    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()

    @classmethod
    def check_password(cls, username, password):
        user = cls.get_by_username(username)
        if not user:
            return False
        return crypt.check(user.password, password)

    def put(self):
        DBSession.add(self)
        DBSession.flush()
