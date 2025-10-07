from pydantic import BaseModel

class Company(BaseModel):
    id: int
    nome: str

class CompanyCreate(BaseModel):
    nome: str
