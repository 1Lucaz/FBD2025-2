from pydantic import BaseModel

class Empresa(BaseModel):
    id: int
    name: str
    cnpj: str
    status : str

class EmpresaCreate(BaseModel):
    name: str
    cnpj: str
    status: str
