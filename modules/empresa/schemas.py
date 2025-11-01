from pydantic import BaseModel

class Empresa(BaseModel):
    id: int
    nome: str
    cnpj: str
    status : str

class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    status: str
