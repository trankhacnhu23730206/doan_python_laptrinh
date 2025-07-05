from fastapi import HTTPException
from sqlalchemy.orm import Session

from products.model import ProductModel
from products.schema import ProductRequest, UpdateProductRequest


def create_product_service(request: ProductRequest, db: Session):
    new_product = ProductModel(
        name=request.name,
        location=request.location,
        price_now=request.price_now,
        note=request.note,
        is_register=request.is_register == 1,
        category_id=request.category_id,
        company_id=request.company_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product



async def get_all_products(db):
    return db.query(ProductModel).all()


async def get_products_by_company_id(company_id: int, db: Session):
    products = db.query(ProductModel).filter(ProductModel.company_id == company_id).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "location": p.location,
            "price_now": p.price_now,
            "note": p.note,
            "is_register": p.is_register,
            "created_at": p.created_at,
            "category_id": p.category_id,
            "company_id": p.company_id,
            "category_name": p.category.name if p.category else None,
            "company_name": {
                "name_company": p.company.name,
                "tele_phone": p.company.phone
            } if p.company else None
        }
        for p in products
    ]


async def get_products_by_category_id(category_id: int, db: Session):
    products = db.query(ProductModel).filter(ProductModel.category_id == category_id).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "location": p.location,
            "price_now": p.price_now,
            "note": p.note,
            "is_register": p.is_register,
            "created_at": p.created_at,
            "category_id": p.category_id,
            "company_id": p.company_id,
            "category_name": p.category.name if p.category else None,
            "company_name": {
                "name_company":p.company.name,
                "tele_phone": p.company.phone
            } if p.company else None
        }
        for p in products
    ]


async def update_product_service(product_id: int, data: UpdateProductRequest, db: Session):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if data.name is not None:
        product.name = data.name
    if data.location is not None:
        product.location = data.location
    if data.price_now is not None:
        product.price_now = data.price_now
    if data.note is not None:
        product.note = data.note
    if data.category_id is not None:
        product.category_id = data.category_id
    if data.company_id is not None:
        product.company_id = data.company_id

    db.commit()
    db.refresh(product)
    return product