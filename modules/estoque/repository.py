from core.db import DataBase
from typing import Any, Dict, List, Optional
from modules.estoque.schemas import EstoqueCreate


class EstoqueRepository:
    QUERY_CREATE = """
        INSERT INTO ESTOQUE (produto_id, quantidade, data_atualizacao) 
        VALUES (%s, %s, NOW()) 
        RETURNING *;
    """
    QUERY_GET_BY_ID = """
        SELECT 
            e.*,
            p.nome AS produto_nome
        FROM ESTOQUE e
        JOIN PRODUTO p ON e.produto_id = p.id
        WHERE e.id = %s;
    """
    QUERY_LIST_ALL = """
        SELECT 
            e.*,
            p.nome AS produto_nome
        FROM ESTOQUE e
        JOIN PRODUTO p ON e.produto_id = p.id
        ORDER BY e.data_atualizacao DESC;
    """

    def save(self, estoque: EstoqueCreate) -> Dict[str, Any]:
        db = DataBase()

        result = db.commit(
            self.QUERY_CREATE,
            (estoque.produto_id, estoque.quantidade),
            returning=True
        )

        if result and isinstance(result, dict):
            return result

        return {"id": None}

    def list_all(self) -> List[Dict[str, Any]]:
        db = DataBase()
        return db.fetchall(self.QUERY_LIST_ALL)

    def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        db = DataBase()
        return db.fetchone(self.QUERY_GET_BY_ID, (id,))