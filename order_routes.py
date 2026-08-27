from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido

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

#rota de criação de pedido
@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"message": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}