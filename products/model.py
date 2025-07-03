from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from core.database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),  unique=True, nullable=False)
    is_register = Column(Boolean, nullable=False)
    phone = Column(String(100),  unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)
