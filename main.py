from fastapi import FastAPI
from auth.route import router as auth_router
from core.database import engine
from core.jwt_security import JWTAuthMiddleware
from users import model
from users.route import router as user_router
import uvicorn

# Tạo bảng nếu chưa có
model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(JWTAuthMiddleware)

app.include_router(router=user_router)
app.include_router(router=auth_router)
@app.get("/")
def health_check():
    return "oke file name"

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9080)