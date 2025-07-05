
from fastapi import APIRouter, status, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.database import getdatabase
from products.schema import ProductRequest
from products.service import create_product_service, get_all_products

router = APIRouter(
    prefix="/product",
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