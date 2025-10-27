from core.db import DataBase

class FornecedorRepository:
    QUERY_CREATE = "INSERT INTO fornecedor (nome, cnpj, status, empresa_id) VALUES (%s, %s, %s, %s) RETURNING id;"
    QUERY_LIST = "SELECT id, nome, cnpj, status, empresa_id FROM fornecedor ORDER BY id;"
    QUERY_GET_BY_ID = "SELECT id, nome, cnpj, status, empresa_id FROM fornecedor WHERE id = %s;"
    QUERY_GET_BY_CNPJ_EMPRESA = "SELECT id FROM fornecedor WHERE empresa_id = %s AND cnpj = %s;"

    def save(self, fornecedor):
        db = DataBase()
        result = db.commit(self.QUERY_CREATE,
                                   (fornecedor.nome, fornecedor.cnpj, fornecedor.status, fornecedor.empresa_id),
                                   returning=True)
        if result:
            return {"id": result[0], "nome": fornecedor.nome, "cnpj": fornecedor.cnpj, "status": fornecedor.status, "empresa_id": fornecedor.empresa_id}
        return {"id": None, "nome": fornecedor.nome, "cnpj": fornecedor.cnpj, "status": fornecedor.status, "empresa_id": fornecedor.empresa_id}

    def list_all(self):
        db = DataBase()
        return db.fetchall(self.QUERY_LIST)

    def get_by_id(self, id):
        db = DataBase()
        return db.fetchone(self.QUERY_GET_BY_ID, (id,))

    def get_by_cnpj_empresa(self, empresa_id, cnpj):
        db = DataBase()
        return db.fetchone(self.QUERY_GET_BY_CNPJ_EMPRESA, (empresa_id, cnpj))