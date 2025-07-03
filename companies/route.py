
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from companies.service import get_all_companies, get_companies_by_category_name
from core.database import getdatabase

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
    responses={404: {"description": "Not found"}},
)

@router.get("/getall")
async def get_categories(db: Session = Depends(getdatabase)):
    return await get_all_companies(db=db)


@router.get("/companies/category/{category_name}")
async def read_companies_by_category(category_name: str, db: Session = Depends(getdatabase)):
    companies = await get_companies_by_category_name(category_name, db)
    return companies