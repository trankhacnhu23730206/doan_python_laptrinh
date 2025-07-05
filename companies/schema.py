from typing import Optional

from pydantic import BaseModel

class CompanyRequest(BaseModel):
    name: str
    email_company: str
    is_register: int
    phone: str
    category_id: int




class UpdateCompanyRequest(BaseModel):
    name: Optional[str]
    email_company: Optional[str]
    phone: Optional[str]
    category_id: Optional[int]