from fastapi.exceptions import HTTPException
from datetime import datetime

from sqlalchemy.orm import Session

from core.security import get_password_hash
from users.model import UserModel


async def create_user_account(data, db):
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=422, detail="Email is already registered with us.")

    new_user = UserModel(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password=get_password_hash(data.password),
        registered_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



async def update_user_info(user_id: int, data, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.first_name is not None:
        user.first_name = data.first_name
    if data.last_name is not None:
        user.last_name = data.last_name
    if data.phone is not None:
        # Optional: Check if phone is unique
        existing_user = db.query(UserModel).filter(UserModel.phone == data.phone, UserModel.id != user_id).first()
        if existing_user:
            raise HTTPException(status_code=422, detail="Phone number already exists.")
        user.phone = data.phone

    user.updated_at = datetime.now()
    db.commit()
    db.refresh(user)
    return user
