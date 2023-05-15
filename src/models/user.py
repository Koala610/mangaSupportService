from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "exclude_from_migrations"}
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255))
    bookmarks_hash = Column(String(255))
    bookmarks_per_page = Column(Integer, default=10)
    is_subscribed = Column(Boolean, default=False)
    last_updated = Column(DateTime, default=datetime.now())


class Admin(Base):
    __tablename__ = 'admins'
    __table_args__ = {"schema": "exclude_from_migrations"}
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    username = Column(String(255))
    password = Column(String(255))
    creation_timestamp = Column(DateTime, default=datetime.now())
    actual_jwt = Column(String(255))

    __table_args__ = (
        UniqueConstraint('username'),
    )

    user: User = relationship('User', foreign_keys=[user_id])

class Support(Base):
    __tablename__ = "supports"
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user: User = relationship('User', foreign_keys=[user_id])
    messages = relationship('Support', back_populates="support")

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, unique=True)
    support_id = Column(Integer, ForeignKey('supports.id'))
    support: Support = relationship('Support', back_populates="messages")
    user_id = Column(Integer, ForeignKey('users.id'))
    user: User = relationship('User', foreign_keys=[user_id])
    message = Column(String(255))
    last_updated = Column(DateTime, default=datetime.now())