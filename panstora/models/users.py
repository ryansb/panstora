import cryptacular.bcrypt

from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
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

    _password = Column('password', Unicode(64))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, username, password, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.password = password

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
    def check_password(cls, username, password):
        user = cls.get_by_username(username)
        if not user:
            return False
        return crypt.check(user.password, password)
