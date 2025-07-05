from fastapi import FastAPI
import uvicorn

from core.database import engine
from core.jwt_security import JWTAuthMiddleware

from users import model as user_model
from companies import model as company_model
from categories import model as category_model
from products import model as product_model
from registrations import model as registration_model

from users.route import router as user_router
from products.route import router as product_router
from auth.route import router as auth_router
from companies.route import router as company_router
from categories.route import router as category_router
from registrations.route import router as registration_router



print("Creating tables...")
# Tạo bảng nếu chưa có
user_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)
company_model.Base.metadata.create_all(bind=engine)
category_model.Base.metadata.create_all(bind=engine)
registration_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)
print("Done.")


app = FastAPI()
app.add_middleware(JWTAuthMiddleware)


app.include_router(router=user_router)
app.include_router(router=auth_router)
app.include_router(router=product_router)
app.include_router(router=company_router)
app.include_router(router=category_router)
app.include_router(router=registration_router)


@app.get("/")
def health_check():
    return "oke file name"

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9080)