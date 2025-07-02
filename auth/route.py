from fastapi import APIRouter, status, Depends, Header
from sqlalchemy.orm import Session

from auth.schema import CreateUserAuthRequest
from auth.service import get_refresh_token, get_token
from core.database import getdatabase

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("/token", status_code=status.HTTP_200_OK)
async def authenticate_user(data: CreateUserAuthRequest, db: Session = Depends(getdatabase)):
    return await get_token(data=data, db=db)

@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh_access_token(refresh_token: str = Header(), db: Session = Depends(getdatabase)):
    return await get_refresh_token(token=refresh_token, db=db)
