from fastapi import APIRouter
from modules.estoque.service import EstoqueService
from modules.estoque.schemas import EstoqueCreate, Estoque

router = APIRouter(prefix="/estoque", tags=["estoque"])

service = EstoqueService()

@router.post("/", response_model=Estoque, status_code=201)
def create_estoque(payload: EstoqueCreate):
    return service.create_estoque(payload)

@router.get("/", response_model=list[Estoque])
def list_estoques():
    return service.list_estoques()

@router.get("/{id}", response_model=Estoque)
def get_estoque(id: int):
    return service.get_estoque_by_id(id)