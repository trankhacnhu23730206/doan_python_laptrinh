
from fastapi import APIRouter, status, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.database import getdatabase
from products.schema import ProductRequest, UpdateProductRequest
from products.service import create_product_service, get_all_products, get_products_by_company_id, \
    get_products_by_category_id, update_product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}},
)

@router.get('/getAll')
async def get_product(db: Session = Depends(getdatabase)):
    products = await get_all_products(db)
    return products

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_product(request: Request, product: ProductRequest, db: Session = Depends(getdatabase)):
    user = request.state.user

    if not user:
        return JSONResponse(status_code=401, content={"detail": "Unauthorized Bearer token of user login"})

    product = await create_product_service(product, db)
    return product


@router.get('/by-company/{company_id}')
async def get_by_company(company_id: int, db: Session = Depends(getdatabase)):
    return await get_products_by_company_id(company_id, db)


@router.get('/by-category/{category_id}')
async def get_by_category(category_id: int, db: Session = Depends(getdatabase)):
    return await get_products_by_category_id(category_id, db)


@router.put('/update/{product_id}', status_code=status.HTTP_200_OK)
async def update_product(
    product_id: int,
    request: Request,
    product_data: UpdateProductRequest,
    db: Session = Depends(getdatabase)
):
    user = request.state.user
    if not user:
        return JSONResponse(status_code=401, content={"detail": "Unauthorized Bearer token of user login"})

    updated_product = await update_product_service(product_id, product_data, db)
    return {
        "message": "Product updated successfully",
        "product": {
            "id": updated_product.id,
            "name": updated_product.name,
            "location": updated_product.location,
            "price_now": updated_product.price_now,
            "note": updated_product.note,
            "category_id": updated_product.category_id,
            "company_id": updated_product.company_id,
            "created_at": updated_product.created_at
        }
    }