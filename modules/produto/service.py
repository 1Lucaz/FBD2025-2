from modules.produto.repository import ProdutoRepository
from modules.produto.schemas import ProdutoCreate
from fastapi import HTTPException
from typing import Any, Dict, List


class ProdutoService:
    def __init__(self):
        self.repo = ProdutoRepository()

    def create_produto(self, dados: ProdutoCreate) -> Dict[str, Any]:
        if not dados.nome or not dados.preco or not dados.tipo_id or not dados.fornecedor_id or not dados.empresa_id:
            raise HTTPException(status_code=400, detail="Campos obrigatórios estão faltando")

        saved = self.repo.save(dados)

        if saved.get("id") is None:
            raise HTTPException(status_code=500, detail="Falha ao salvar o produto no banco de dados.")

        return saved

    def list_produtos(self) -> List[Dict[str, Any]]:
        return self.repo.list_all()

    def get_produto_by_id(self, id: int) -> Dict[str, Any]:
        produto = self.repo.get_by_id(id)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return produto

    def list_produtos_by_empresa(self, empresa_id: int) -> List[Dict[str, Any]]:
        return self.repo.list_by_empresa(empresa_id)