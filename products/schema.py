from typing import Optional

from pydantic import BaseModel

class ProductRequest(BaseModel):
    name: str
    location: str
    price_now: int
    note: str
    is_register: bool

    category_id: int
    company_id: int


class UpdateProductRequest(BaseModel):
    name: Optional[str]
    location: Optional[str]
    price_now: Optional[int]
    note: Optional[str]
    category_id: Optional[int]
    company_id: Optional[int]
