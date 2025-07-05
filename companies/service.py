from fastapi import HTTPException
from sqlalchemy.orm import Session

from categories.model import CategoryModel
from companies.model import CompanyModel
from companies.schema import CompanyRequest


async def get_all_companies(db):
    return db.query(CompanyModel).all()

async def get_companies_by_category_name(category_name: str, db: Session):
    return (
        db.query(CompanyModel)
        .join(CategoryModel)
        .filter(CategoryModel.name == category_name)
        .all()
    )


async def create_company_service(company: CompanyRequest, db: Session, user_id: int):
    # Kiểm tra category có tồn tại không
    category = db.query(CategoryModel).filter(CategoryModel.id == company.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # Kiểm tra tên công ty có bị trùng không
    existing_company = db.query(CompanyModel).filter(CompanyModel.name == company.name).first()
    if existing_company:
        raise HTTPException(status_code=400, detail="Company already exists")

    # Tạo mới công ty
    new_company = CompanyModel(
        name=company.name,
        email_company=company.email_company,
        is_register = company.is_register == 1,
        phone = company.phone,
        user_id = user_id,
        category_id=company.category_id
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company