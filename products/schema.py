from pydantic import BaseModel

class CreateProductRequest(BaseModel):
    name: str
    is_register: bool
    phone: str
    category_id: int
    company_id: int
