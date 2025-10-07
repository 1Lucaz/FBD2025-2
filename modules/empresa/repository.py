from core.db import DataBase
from modules.empresa.schemas import EmpresaCreate


class EmpresaRepository:
    QUERY_EMPRESAS = "SELECT id, name, cnpj, status FROM empresas ORDER BY name"
    QUERY_EMPRESA_ID = "SELECT id, name, cnpj, status FROM empresas WHERE id = %s"
    QUERY_CREATE_EMPRESA = 'INSERT INTO empresas (name, cnpj, status) VALUES (%s, %s, %s) RETURNING id, name, cnpj, status;'

    def get_all(self):
        db = DataBase()
        empresas = db.execute(self.QUERY_EMPRESAS)
        results = []
        for empresa in empresas:
            results.append({"id": empresa[0], "name": empresa[1], "cnpj": empresa[2], "status": empresa[3]})
        return results

    def save(self, empresa: EmpresaCreate):
        db = DataBase()
        empresa_data = (empresa.name, empresa.cnpj, empresa.status)
        result = db.commit(self.QUERY_CREATE_EMPRESA, empresa_data)
        if result:
            return {"id": result[0], "name": result[1], "cnpj": result[2], "status": result[3]}
        return {}

    def get_id(self, id: int):
        db = DataBase()
        empresa = db.execute(self.QUERY_EMPRESA_ID, (id,), many=False)
        if empresa:
            return {"id": empresa[0], "name": empresa[1], "cnpj": empresa[2], "status": empresa[3]}
        return {}