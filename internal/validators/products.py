from pydantic import BaseModel


class ProductRequest(BaseModel):
    name: str
    description: str
    price: int
    category_id: int
    quantity: int
    weight: float
