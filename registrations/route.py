
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from core.database import getdatabase
from registrations.service import get_product_registration_detail

router = APIRouter(
    prefix="/product-detail",
    tags=["Companies"],
    responses={404: {"description": "Not found"}},
)

@router.get("/getall")
async def get_categories(db: Session = Depends(getdatabase)):
    return await get_product_registration_detail(db=db)

