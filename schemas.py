from pydantic import BaseModel
from typing import Optional 

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes = True

class PedidoSchema(BaseModel):
    #só irá chamar o usuario que fez o pedido
    #pois o status e preco são definidos automaticamente
    id_usuario: int

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True