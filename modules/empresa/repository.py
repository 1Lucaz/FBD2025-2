from core.db import DataBase

class EmpresaRepository:
    QUERY_CREATE = "INSERT INTO empresa (nome, cnpj, status) VALUES (%s, %s, %s) RETURNING id;"
    QUERY_LIST = "SELECT id, nome, cnpj, status FROM empresa ORDER BY id;"
    QUERY_GET_BY_ID = "SELECT id, nome, cnpj, status FROM empresa WHERE id = %s;"
    QUERY_GET_BY_CNPJ = "SELECT id FROM empresa WHERE cnpj = %s;"

    def save(self, empresa):
        db = DataBase()
        
        result = db.commit(self.QUERY_CREATE, (empresa.nome, empresa.cnpj, empresa.status), returning=True)
        if result:

            if isinstance(result, tuple) or isinstance(result, list):
                return {"id": result[0], "nome": empresa.nome, "cnpj": empresa.cnpj, "status": empresa.status}

        return {"id": None, "nome": empresa.nome, "cnpj": empresa.cnpj, "status": empresa.status}

    def list_all(self):
        db = DataBase()
        return db.fetchall(self.QUERY_LIST)

    def get_by_id(self, id):
        db = DataBase()
        return db.fetchone(self.QUERY_GET_BY_ID, (id,))

    def get_by_cnpj(self, cnpj):
        db = DataBase()
        return db.fetchone(self.QUERY_GET_BY_CNPJ, (cnpj,))