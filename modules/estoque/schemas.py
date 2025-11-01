from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Estoque(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    data_atualizacao: datetime
    produto_nome: Optional[str] = None

class EstoqueCreate(BaseModel):
    produto_id: int
    quantidade: int