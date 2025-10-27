from fastapi import APIRouter
from modules.tipo.service import TipoService
from modules.tipo.schemas import TipoCreate, TipoBase

router = APIRouter(prefix="/tipo", tags=["tipo"])

service = TipoService()

@router.post("/", response_model=TipoBase, status_code=201)
def create_tipo(payload: TipoCreate):
    return service.create_tipo(payload)

@router.get("/", response_model=list[TipoBase])
def list_tipos():
    return service.list_tipos()

@router.get("/{id}", response_model=TipoBase)
def get_tipo(id: int):
    return service.get_tipo_by_id(id)