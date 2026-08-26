from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

# rotas de requisição
@order_router.get("/")
# toda função que for assíncrona deve ser declarada com async def
async def orders():
    """
    Essa é a rota de pedidos
    """
    return {
        "message": "Você acessou a rota de pedidos"
    }