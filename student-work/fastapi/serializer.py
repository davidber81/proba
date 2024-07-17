from typing import List, Union
from pydantic import BaseModel

class PydanticUser(BaseModel):
    username: str
    password: str


class PydanticShop(BaseModel):
    name: str


class PydanticProduct(BaseModel):
    name: str
    articule: str
    description: str
    price: float
    photo: str = "" 

class PydanticProductUpdate(BaseModel):
    name: Union[str, None] = ""
    articule: Union[str, None] = ""
    description: Union[str, None] = ""
    price: Union[float, None] = None
    photo: Union[str, None] = "" 


class PydanticProductsArray(BaseModel):
    prodcuts: List[PydanticProduct]