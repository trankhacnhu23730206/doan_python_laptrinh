from pydantic import BaseModel

class ProductRequest(BaseModel):
    name: str
    location: str
    price_now: int
    note: str
    is_register: bool

    category_id: int
    company_id: int
