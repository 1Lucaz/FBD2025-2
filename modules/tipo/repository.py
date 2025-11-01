from core.db import DataBase

class TipoRepository:
    QUERY_CREATE = "INSERT INTO tipo (nome, cod_tipo, empresa_id) VALUES (%s, %s, %s) RETURNING id;"
    QUERY_LIST = "SELECT id, nome, cod_tipo, empresa_id FROM tipo ORDER BY id;"
    QUERY_GET_BY_ID = "SELECT id, nome, cod_tipo, empresa_id FROM tipo WHERE id = %s;"
    QUERY_GET_BY_COD_EMPRESA = "SELECT id FROM tipo WHERE empresa_id = %s AND cod_tipo = %s;"

    def save(self, tipo):
        db = DataBase()
        try:
            result = db.commit(self.QUERY_CREATE, (tipo.nome, tipo.cod_tipo, tipo.empresa_id), returning=True)
            if result and isinstance(result, dict) and "id" in result:
                return {
                    "id": result["id"],
                    "nome": tipo.nome,
                    "cod_tipo": tipo.cod_tipo,
                    "empresa_id": tipo.empresa_id
                }
            raise Exception("Falha ao inserir tipo: retorno inesperado do banco.")
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

    def get_by_cod_empresa(self, empresa_id, cod_tipo):
        db = DataBase()
        try:
            return db.fetchone(self.QUERY_GET_BY_COD_EMPRESA, (empresa_id, cod_tipo))
        finally:
            db.close()
