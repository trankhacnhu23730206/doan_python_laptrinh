from datetime import datetime

from pydantic import BaseModel

class CreateProductRequest(BaseModel):
    user_id: int
    product_id: int
    import_price: int
    quantity: int
    import_date: datetime
    note: str
