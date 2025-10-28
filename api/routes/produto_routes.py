from fastapi import APIRouter
from modules.produto.service import ProdutoService
from modules.produto.schemas import ProdutoCreate, Produto

router = APIRouter(prefix="/produto", tags=["produto"])

service = ProdutoService()

@router.post("/", response_model=Produto, status_code=201)
def create_produto(payload: ProdutoCreate):
    return service.create_produto(payload)

@router.get("/", response_model=list[Produto])
def list_produtos():
    return service.list_produtos()

@router.get("/{id}", response_model=Produto)
def get_produto(id: int):
    return service.get_produto_by_id(id)

@router.get("/empresa/{id_empresa}/produtos", response_model=list[Produto])
def list_produtos_by_empresa(id_empresa: int):
    return service.list_produtos_by_empresa(id_empresa)