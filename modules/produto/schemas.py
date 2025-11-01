from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float
    tipo_id: int
    fornecedor_id: int
    empresa_id: int
    tipo_nome: Optional[str] = None
    fornecedor_nome: Optional[str] = None

class ProdutoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    tipo_id: int
    fornecedor_id: int
    empresa_id: int