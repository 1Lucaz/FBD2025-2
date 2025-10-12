from pydantic import BaseModel

class Fornecedor(BaseModel):
    id: int
    empresa_id : int
    nome: str
    cnpj: str
    status : str

class FornecedorCreate(BaseModel):
    empresa_id: int
    nome: str
    cnpj: str
    status: str

