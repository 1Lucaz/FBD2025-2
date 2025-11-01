from modules.tipo.repository import TipoRepository
from modules.tipo.schemas import TipoCreate
from fastapi import HTTPException

class TipoService:
    def __init__(self):
        self.repo = TipoRepository()

    def create_tipo(self, dados: TipoCreate):

        if not dados.nome or not dados.cod_tipo or not dados.empresa_id:
            raise HTTPException(status_code=400, detail="Campos 'nome', 'cod_tipo' e 'empresa_id' são obrigatórios")


        existing = self.repo.get_by_cod_empresa(dados.empresa_id, dados.cod_tipo)
        if existing:
            raise HTTPException(status_code=409, detail="Código de tipo já cadastrado para esta empresa")

        saved = self.repo.save(dados)
        return saved

    def list_tipos(self):
        return self.repo.list_all()

    def get_tipo_by_id(self, id: int):
        tipo = self.repo.get_by_id(id)
        if not tipo:
            raise HTTPException(status_code=404, detail="Tipo não encontrado")
        return tipo