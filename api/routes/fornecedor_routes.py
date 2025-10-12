from fastapi import APIRouter
from modules.fornecedor.service import FornecedorService
from modules.fornecedor.schemas import FornecedorCreate, Fornecedor

router = APIRouter(prefix="/fornecedor", tags=["fornecedor"])

service = FornecedorService()

@router.post("/", response_model=Fornecedor, status_code=201)
def create_fornecedor(payload: FornecedorCreate):
    return service.create_fornecedor(payload)

@router.get("/", response_model=list[Fornecedor])
def list_fornecedores():
    return service.list_fornecedores()

@router.get("/{id}", response_model=Fornecedor)
def get_fornecedor(id: int):
    return service.get_fornecedor_by_id(id)