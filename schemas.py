from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password : str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    class config:
        from_attributes = True


class RestaurantCreate(BaseModel):
    name: str
    location : str
    owner_id : str


class RestaurantOut(BaseModel):
    id: int
    name: str
    location : str
    class config:
        from_attributes= True



class DishCreate(BaseModel):
    name: str
    price: int
    restaurant_id: int

class DishOut(BaseModel):
    id: int
    name: str
    price: int
    class Config:
        from_attributes= True

