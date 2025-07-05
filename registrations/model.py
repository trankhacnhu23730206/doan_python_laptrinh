from sqlalchemy import Column, ForeignKey, DECIMAL, Integer, Date, Text, DateTime, func
from core.database import Base

class ProductRegistrationModel(Base):
    __tablename__ = "product_registrations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    price_now = Column(DECIMAL(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_register_at = Column(DateTime, nullable=False)
