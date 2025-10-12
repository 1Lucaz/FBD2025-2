from fastapi import APIRouter
from modules.empresa.service import EmpresaService
from modules.empresa.schemas import EmpresaCreate, Empresa

router = APIRouter(prefix="/empresa", tags=["empresa"])

service = EmpresaService()

@router.post("/", response_model=Empresa, status_code=201)
def create_empresa(payload: EmpresaCreate):
    return service.create_empresa(payload)

@router.get("/", response_model=list[Empresa])
def list_empresas():
    return service.list_empresas()

@router.get("/{id}", response_model=Empresa)
def get_empresa(id: int):
    return service.get_empresa_by_id(id)