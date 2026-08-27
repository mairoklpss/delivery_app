from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema

# roteador para autenticação
# prefixo: caminho da rota, tags: subtitulo da documentação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get('/')
async def home():
    """
    Essa é a rota de autenticação
    """
    return {
        "message": "Você acessou a rota de autenticação"
    }

@auth_router.post('/criar_conta')
#função de criar conta, recebe email e senha como parâmetros e ambos sao STRING
async def criar_conta(usuario_schema: UsuarioSchema, session=Depends(pegar_sessao)):

    # verificar se o usuário com o mesmo email já existe no banco de dados
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        # ja existe algum usuario
        raise HTTPException(status_code=400, detail="E-mail de Usuário já cadastrado") 
    else: 
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        # vai salvar o usuario
        session.commit()
        return { "message": f"Usuário criado com sucesso: {usuario_schema.email}"}

    