
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/product",
    tags=["Products"],
    responses={404: {"description": "Not found"}},
)

@router.get('/getproducts')
async def get_product():
    payload = {"message": "Product get all"}
    return JSONResponse(content=payload)

@router.post('/createproduct', status_code=status.HTTP_201_CREATED)
async def get_product():
    payload = {"message": "Product create successfully"}
    return JSONResponse(content=payload)