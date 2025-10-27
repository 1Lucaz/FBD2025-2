from typing import Optional

from fastapi import APIRouter

from modules.company import schemas
from modules.company.schemas import CompanyCreate
from modules.company.service import CompanyService

router = APIRouter(prefix="/company", tags=["Company"])

@router.get("/listar_companhias", response_model=list[schemas.Company])
def list_companies():
    service = CompanyService()
    return service.get_companies()

@router.get("/companhia_id_{id}/", response_model=Optional[schemas.Company])
def get_company_by_id(id: int):
    service = CompanyService()
    return service.get_company_id(id)

@router.post("/", response_model=schemas.Company)
def add_company(company: CompanyCreate):
    service = CompanyService()
    return service.create_company(company)
