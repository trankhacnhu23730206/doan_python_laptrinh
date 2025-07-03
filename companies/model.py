from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base

class CompanyModel(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),  unique=True, nullable=False)
    email_company = Column(String(255), unique=True, index=True)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("CategoryModel", back_populates="companies")
