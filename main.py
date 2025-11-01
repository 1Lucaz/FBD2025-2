from fastapi import FastAPI

# Importações de rotas existentes
from api.routes.empresa_routes import router as empresa_router
from api.routes.tipo_routes import router as tipo_router
from api.routes.fornecedor_routes import router as fornecedor_router

from api.routes.produto_routes import router as produto_router
from api.routes.estoque_routes import router as estoque_router

app = FastAPI(title = "TESTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")


app.include_router(empresa_router)
app.include_router(tipo_router)
app.include_router(fornecedor_router)
app.include_router(produto_router)
app.include_router(estoque_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}