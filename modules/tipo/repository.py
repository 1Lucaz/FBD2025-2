from core.db import DataBase

class TipoRepository:
    QUERY_CREATE = "INSERT INTO tipo (nome, cod_tipo, empresa_id) VALUES (%s, %s, %s) RETURNING id;"
    QUERY_LIST = "SELECT id, nome, cod_tipo, empresa_id FROM tipo ORDER BY id;"
    QUERY_GET_BY_ID = "SELECT id, nome, cod_tipo, empresa_id FROM tipo WHERE id = %s;"
    QUERY_GET_BY_COD_EMPRESA = "SELECT id FROM tipo WHERE empresa_id = %s AND cod_tipo = %s;"

    def save(self, tipo):
        db = DataBase()
        result = db.commit(self.QUERY_CREATE, (tipo.nome, tipo.cod_tipo, tipo.empresa_id), returning=True)
        if result:
            return {"id": result[0], "nome": tipo.nome, "cod_tipo": tipo.cod_tipo, "empresa_id": tipo.empresa_id}
        return {"id": None, "nome": tipo.nome, "cod_tipo": tipo.cod_tipo, "empresa_id": tipo.empresa_id}

    def list_all(self):
        db = DataBase()
        return db.fetchall(self.QUERY_LIST)

    def get_by_id(self, id):
        db = DataBase()
        return db.fetchone(self.QUERY_GET_BY_ID, (id,))

    def get_by_cod_empresa(self, empresa_id, cod_tipo):
        db = DataBase()
        return db.fetchone(self.QUERY_GET_BY_COD_EMPRESA, (empresa_id, cod_tipo))