from modules.empresa.repository import EmpresaRepository
from modules.empresa.schemas import EmpresaCreate
from fastapi import HTTPException

class EmpresaService:
    def __init__(self):
        self.repo = EmpresaRepository()

    def create_empresa(self, dados: EmpresaCreate):

        if not dados.nome or not dados.cnpj or not dados.status:
            raise HTTPException(status_code=400, detail="Campos 'nome', 'cnpj' e 'status' são obrigatórios")

        existing = self.repo.get_by_cnpj(dados.cnpj)
        if existing:
            raise HTTPException(status_code=409, detail="CNPJ da empresa já cadastrado")

        saved = self.repo.save(dados)
        return saved

    def list_empresas(self):
        return self.repo.list_all()

    def get_empresa_by_id(self, id: int):
        empresa = self.repo.get_by_id(id)
        if not empresa:
            raise HTTPException(status_code=404, detail="Empresa não encontrada")
        return empresa