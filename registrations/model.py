from sqlalchemy import Column, ForeignKey, DECIMAL, Integer, Date, Text, DateTime, func
from core.database import Base

class ProductRegistrationModel(Base):
    __tablename__ = "product_registrations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    import_price = Column(DECIMAL(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    import_date = Column(Date, nullable=False)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
