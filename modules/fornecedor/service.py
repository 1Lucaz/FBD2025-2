from http import HTTPStatus

from modules.fornecedor.repository import FornecedorRepository
from modules.fornecedor.schemas import FornecedorCreate
from fastapi import HTTPException

class FornecedorService:
    def __init__(self):
        self.repo = FornecedorRepository()

    def create_fornecedor(self, dados: FornecedorCreate):
        if not dados.nome or not dados.cnpj or not dados.status or not dados.empresa_id:
            raise HTTPException(status_code=400, detail="Campos 'nome', 'cnpj', 'status' e 'empresa_id' são obrigatórios")

        # checar unicidade do cnpj dentro da mesma empresa
        existing = self.repo.get_by_cnpj_empresa(dados.empresa_id, dados.cnpj)
        if existing:
            raise HTTPException(status_code=409, detail="CNPJ do fornecedor já cadastrado para esta empresa")

        saved = self.repo.save(dados)
        return saved

    def list_fornecedores(self):
        return self.repo.list_all()

    def get_fornecedor_by_id(self, id: int):
        fornecedor = self.repo.get_by_id(id)
        if not fornecedor:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Fornecedor não encontrado")
        return fornecedor