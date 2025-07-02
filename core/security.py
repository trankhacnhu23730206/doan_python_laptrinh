from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from starlette.authentication import AuthCredentials, UnauthenticatedUser
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from fastapi import Depends

from core.database import getdatabase
from users.model import UserModel

settings = getdatabase()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(data, expiry: timedelta):
    payload = data.copy()
    expire_in = datetime.now(timezone.utc) + expiry  # ✅ nên dùng UTC
    payload.update({"exp": expire_in})
    return jwt.encode(payload, "trankhacnhutranbaobach", algorithm="HS256")


async def create_refresh_token(data):
    return jwt.encode(data, "trankhacnhutranbaobach", algorithm="HS256")


def get_token_payload(token):
    try:
        payload = jwt.decode(token, "trankhacnhutranbaobach", algorithms=["HS256"])
    except JWTError:
        return None
    return payload


def get_current_user(token: str = Depends(oauth2_scheme), db=None):
    payload = get_token_payload(token)
    if not payload or type(payload) is not dict:
        return None

    user_id = payload.get('id', None)
    if not user_id:
        return None

    if not db:
        db = next(getdatabase())

    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    return user

#
# class JWTAuth:
#
#     # @staticmethod
#     @staticmethod
#     async def authenticate(conn):
#         guest = AuthCredentials(['unauthenticated']), UnauthenticatedUser()
#
#         try:
#             if 'authorization' not in conn.headers:
#                 return guest
#
#             token = conn.headers.get('authorization').split(' ')[1]  # Bearer token_hash
#             if not token:
#                 return guest
#
#             user = await get_current_user(token=token)
#
#             if not user:
#                 return guest
#
#             return AuthCredentials('authenticated'), user
#
#         except Exception as e:
#                 print("[ERROR] Exception in middleware:", str(e))
#                 # traceback.print_exc()
#                 return guest
