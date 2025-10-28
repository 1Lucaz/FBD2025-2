from modules.estoque.repository import EstoqueRepository
from modules.estoque.schemas import EstoqueCreate
from fastapi import HTTPException
from typing import Any, Dict, List


class EstoqueService:
    def __init__(self):
        self.repo = EstoqueRepository()

    def create_estoque(self, dados: EstoqueCreate) -> Dict[str, Any]:
        if not dados.produto_id or dados.quantidade is None:
            raise HTTPException(status_code=400, detail="Campos 'produto_id' e 'quantidade' são obrigatórios")

        saved = self.repo.save(dados)

        if saved.get("id") is None:
            raise HTTPException(status_code=500, detail="Falha ao salvar o registro de estoque no banco de dados.")

        return saved

    def list_estoques(self) -> List[Dict[str, Any]]:
        return self.repo.list_all()

    def get_estoque_by_id(self, id: int) -> Dict[str, Any]:
        estoque = self.repo.get_by_id(id)
        if not estoque:
            raise HTTPException(status_code=404, detail="Registro de estoque não encontrado")
        return estoque