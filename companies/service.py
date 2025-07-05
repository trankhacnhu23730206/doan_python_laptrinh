from fastapi import HTTPException
from sqlalchemy.orm import Session

from categories.model import CategoryModel
from companies.model import CompanyModel
from companies.schema import CompanyRequest
from companies.schema import UpdateCompanyRequest


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
        phone = company.phone,
        user_id = user_id,
        category_id=company.category_id
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company




async def update_company_service(company_id: int, data: UpdateCompanyRequest, db: Session, user_id: int):
    company = db.query(CompanyModel).filter(CompanyModel.id == company_id, CompanyModel.user_id == user_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found or access denied")

    if data.name is not None:
        company.name = data.name
    if data.email_company is not None:
        company.email_company = data.email_company
    if data.phone is not None:
        company.phone = data.phone
    if data.category_id is not None:
        # Kiểm tra category tồn tại không
        category = db.query(CategoryModel).filter(CategoryModel.id == data.category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        company.category_id = data.category_id

    db.commit()
    db.refresh(company)
    return company