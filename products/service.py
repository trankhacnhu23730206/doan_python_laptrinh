from sqlalchemy.orm import Session

from products.model import ProductModel
from products.schema import ProductRequest


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

