
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime, func
from sqlalchemy.orm import relationship

from core.database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),  unique=True, nullable=False)
    location = Column(String(100), nullable=False)
    price_now = Column(Integer, nullable=False)

    note = Column(Text, nullable=True)
    is_register = Column(Boolean, nullable=False)


    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)

    created_at = Column(DateTime, nullable=False, server_default=func.now())

    # Quan hệ với bảng categories và companies
    category = relationship("CategoryModel", back_populates="products")
    company = relationship("CompanyModel", back_populates="products")