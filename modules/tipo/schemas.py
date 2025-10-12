from pydantic import BaseModel, Field

class TipoBase(BaseModel):
    id: int
    nome: str
    cod_tipo: str
    empresa_id: int

class TipoCreate(TipoBase):
    nome: str
    cod_tipo : str
    empresa_id : str