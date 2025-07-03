from sqlalchemy.orm import Session

from categories.model import CategoryModel
from companies.model import CompanyModel


async def get_all_companies(db):
    return db.query(CompanyModel).all()

async def get_companies_by_category_name(category_name: str, db: Session):
    return (
        db.query(CompanyModel)
        .join(CategoryModel)
        .filter(CategoryModel.name == category_name)
        .all()
    )