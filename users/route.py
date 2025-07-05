
from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.database import getdatabase
from users.schema import CreateUserRequest, UpdateUserRequest
from users.service import create_user_account, update_user_info

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(getdatabase)):
    await create_user_account(data=data, db=db)
    payload = {"message": "User account has been succesfully created."}
    return JSONResponse(content=payload)


@router.get('/me', status_code=status.HTTP_200_OK)
async def check_profile(request: Request):
    user = request.state.user

    if not user:
        return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

    return {
        "message": "Profile accessed successfully",
        "user_id": user["id"]
    }

@router.put('/update', status_code=status.HTTP_200_OK)
async def update_user(data: UpdateUserRequest, request: Request, db: Session = Depends(getdatabase)):
    user = request.state.user
    if not user:
        return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

    updated_user = await update_user_info(user_id=user["id"], data=data, db=db)
    return {
        "message": "User profile updated successfully",
        "user": {
            "id": updated_user.id,
            "first_name": updated_user.first_name,
            "last_name": updated_user.last_name,
            "email": updated_user.email,
            "phone": updated_user.phone,
            "updated_at": str(updated_user.updated_at)
        }
    }