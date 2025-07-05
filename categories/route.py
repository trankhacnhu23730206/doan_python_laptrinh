
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from categories.service import get_all_categories
from core.database import getdatabase

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    responses={404: {"description": "Not found"}},
)

@router.get("/getall")
async def get_categories(db: Session = Depends(getdatabase)):
    return await get_all_categories(db=db)


