from pydantic import BaseModel

class Fornecedor(BaseModel):
    id: int
    empresa_id : int
    nome: str
    cnpj: str
    status : str

class FornecedorCreate(BaseModel):
    nome: str
    cnpj: str
    status: str
    empresa_id: int
