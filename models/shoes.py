from pydantic import BaseModel

class Shoes(BaseModel):
    image: str
    name: str
    description: str
    price: str
    color: str