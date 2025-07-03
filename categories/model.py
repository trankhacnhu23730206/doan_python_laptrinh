from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base

class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),  unique=True, nullable=False)


    companies = relationship("CompanyModel", back_populates="category")

