from fastapi import APIRouter
from modules.tipo.service import TipoService
from modules.tipo.schemas import TipoCreate, TipoBase

router = APIRouter(prefix="/tipo", tags=["tipo"])

service = TipoService()

@router.post("/criar_tipos", response_model=TipoBase, status_code=201)
def create_tipo(payload: TipoCreate):
    return service.create_tipo(payload)

@router.get("/listar_tipos", response_model=list[TipoBase])
def list_tipos():
    return service.list_tipos()

@router.get("/tipo_por_id_{id}", response_model=TipoBase)
def get_tipo(id: int):
    return service.get_tipo_by_id(id)