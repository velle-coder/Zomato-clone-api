from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)


class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User")
    dishes = relationship("Dish", back_populates="restaurant")


class Dish(Base):
    __tablename__ = "dishes"
    id =  Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

    restaurant =  relationship("Restaurant", back_populates="dishes")

