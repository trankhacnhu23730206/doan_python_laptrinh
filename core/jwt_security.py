from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from jose import jwt, JWTError

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Mặc định gán user là None
        request.state.user = None

        auth_header = request.headers.get("authorization")

        if auth_header:
            try:
                scheme, token = auth_header.split(" ")
                if scheme.lower() != "bearer":
                    raise ValueError("Invalid token scheme")

                payload = jwt.decode(token, "trankhacnhutranbaobach", algorithms=["HS256"])
                user_id = payload.get("id")

                # Gán user ID vào request.state nếu có
                if user_id:
                    request.state.user = {"id": user_id}

            except (JWTError, ValueError, IndexError) as e:
                print("JWT Decode error:", e)
                # Optional: trả 401 luôn nếu bạn muốn
                # return JSONResponse(status_code=401, content={"detail": "Invalid token"})

        # Cho request tiếp tục nếu không có token hoặc token lỗi
        response = await call_next(request)
        return response
