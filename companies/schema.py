from pydantic import BaseModel

class CompanyRequest(BaseModel):
    name: str
    email_company: str
    is_register: int
    phone: str
    category_id: int
