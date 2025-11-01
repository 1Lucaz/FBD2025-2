from core.db import DataBase
from typing import Any, Dict, List, Optional
from modules.produto.schemas import ProdutoCreate


class ProdutoRepository:
    QUERY_CREATE = """
        INSERT INTO PRODUTO (nome, descricao, preco, tipo_id, fornecedor_id, empresa_id) 
        VALUES (%s, %s, %s, %s, %s, %s) 
        RETURNING id;
    """
    QUERY_GET_BY_ID = """
        SELECT
            p.*,
            t.nome AS tipo_nome,
            f.nome AS fornecedor_nome
        FROM PRODUTO p
        JOIN TIPO t ON p.tipo_id = t.id
        JOIN FORNECEDOR f ON p.fornecedor_id = f.id
        WHERE p.id = %s;
    """
    QUERY_LIST_ALL = """
        SELECT
            p.*,
            t.nome AS tipo_nome,
            f.nome AS fornecedor_nome
        FROM PRODUTO p
        JOIN TIPO t ON p.tipo_id = t.id
        JOIN FORNECEDOR f ON p.fornecedor_id = f.id
        ORDER BY p.id;
    """
    QUERY_LIST_BY_EMPRESA = """
        SELECT
            p.*,
            t.nome AS tipo_nome,
            f.nome AS fornecedor_nome
        FROM PRODUTO p
        JOIN TIPO t ON p.tipo_id = t.id
        JOIN FORNECEDOR f ON p.fornecedor_id = f.id
        WHERE p.empresa_id = %s
        ORDER BY p.id;
    """

    def save(self, produto: ProdutoCreate) -> Dict[str, Any]:
        db = DataBase()
        try:
            result = db.commit(
                self.QUERY_CREATE,
                (
                    produto.nome,
                    produto.descricao,
                    produto.preco,
                    produto.tipo_id,
                    produto.fornecedor_id,
                    produto.empresa_id
                ),
                returning=True
            )

            if result and isinstance(result, dict) and "id" in result:
                return {
                    "id": result["id"],
                    "nome": produto.nome,
                    "descricao": produto.descricao,
                    "preco": produto.preco,
                    "tipo_id": produto.tipo_id,
                    "fornecedor_id": produto.fornecedor_id,
                    "empresa_id": produto.empresa_id,
                    "tipo_nome": None,
                    "fornecedor_nome": None,
                }

            raise Exception("Falha ao inserir produto: retorno inesperado do banco.")
        finally:
            db.close()

    def list_all(self) -> List[Dict[str, Any]]:
        db = DataBase()
        try:
            return db.fetchall(self.QUERY_LIST_ALL)
        finally:
            db.close()

    def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        db = DataBase()
        try:
            return db.fetchone(self.QUERY_GET_BY_ID, (id,))
        finally:
            db.close()

    def list_by_empresa(self, empresa_id: int) -> List[Dict[str, Any]]:
        db = DataBase()
        try:
            return db.fetchall(self.QUERY_LIST_BY_EMPRESA, (empresa_id,))
        finally:
            db.close()
