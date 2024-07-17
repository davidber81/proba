
from datetime import datetime
from .base import Base
from sqlalchemy import DateTime, Float, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    token = Column(String(255), unique=True)
    user = Column(ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    token = relationship("Token")
    shop = Column(Integer, ForeignKey("shops.id"))


class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    name = Column(String(255), unique=True)
    owner_id = relationship("User", backref='shops', uselist=False)


class Product(Base):
    __tablename__ = "products"
     
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    name = Column(String(255))
    articule = Column(String(255), unique=True)
    description = Column(String(255))
    price = Column(Float)
    photo = Column(String(100))
    shop = Column(ForeignKey("shops.id"))