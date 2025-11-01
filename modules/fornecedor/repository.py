from core.db import DataBase

class FornecedorRepository:
    QUERY_CREATE = "INSERT INTO fornecedor (nome, cnpj, status, empresa_id) VALUES (%s, %s, %s, %s) RETURNING id;"
    QUERY_LIST = "SELECT id, nome, cnpj, status, empresa_id FROM fornecedor ORDER BY id;"
    QUERY_GET_BY_ID = "SELECT id, nome, cnpj, status, empresa_id FROM fornecedor WHERE id = %s;"
    QUERY_GET_BY_CNPJ_EMPRESA = "SELECT id FROM fornecedor WHERE empresa_id = %s AND cnpj = %s;"

    def save(self, fornecedor):
        db = DataBase()
        try:
            result = db.commit(
                self.QUERY_CREATE,
                (fornecedor.nome, fornecedor.cnpj, fornecedor.status, fornecedor.empresa_id),
                returning=True
            )
            if result and isinstance(result, dict) and "id" in result:
                return {
                    "id": result["id"],
                    "nome": fornecedor.nome,
                    "cnpj": fornecedor.cnpj,
                    "status": fornecedor.status,
                    "empresa_id": fornecedor.empresa_id
                }
            raise Exception("Falha ao inserir fornecedor: retorno inesperado do banco.")
        finally:
            db.close()

    def list_all(self):
        db = DataBase()
        try:
            return db.fetchall(self.QUERY_LIST)
        finally:
            db.close()

    def get_by_id(self, id):
        db = DataBase()
        try:
            return db.fetchone(self.QUERY_GET_BY_ID, (id,))
        finally:
            db.close()

    def get_by_cnpj_empresa(self, empresa_id, cnpj):
        db = DataBase()
        try:
            return db.fetchone(self.QUERY_GET_BY_CNPJ_EMPRESA, (empresa_id, cnpj))
        finally:
            db.close()
