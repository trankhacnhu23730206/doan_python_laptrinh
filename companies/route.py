
from fastapi import APIRouter, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from companies.schema import CompanyRequest, UpdateCompanyRequest
from companies.service import (
    get_all_companies,
    get_companies_by_category_name,
    create_company_service, \
    update_company_service
)
from core.database import getdatabase

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
    responses={404: {"description": "Not found"}},
)

@router.get("/getall")
async def get_categories(db: Session = Depends(getdatabase)):
    return await get_all_companies(db=db)


@router.get("/category/{category_name}")
async def read_companies_by_category(category_name: str, db: Session = Depends(getdatabase)):
    companies = await get_companies_by_category_name(category_name, db)
    return companies

@router.post("/create")
async def create_company(request: Request, company: CompanyRequest, db: Session = Depends(getdatabase)):
    user = request.state.user

    if not user:
        return JSONResponse(status_code=401, content={"detail": "Unauthorized Bearer token of user login"})

    return await create_company_service(company, db, user["id"])



@router.put("/update/{company_id}")
async def update_company(
    company_id: int,
    request: Request,
    company_data: UpdateCompanyRequest,
    db: Session = Depends(getdatabase)
):
    user = request.state.user

    if not user:
        return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

    updated_company = await update_company_service(company_id, company_data, db, user["id"])
    return {
        "message": "Company updated successfully",
        "company": {
            "id": updated_company.id,
            "name": updated_company.name,
            "email_company": updated_company.email_company,
            "phone": updated_company.phone,
            "category_id": updated_company.category.name
        }
    }