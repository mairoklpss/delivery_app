from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context

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
async def criar_conta(email: str, senha: str, nome: str, session=Depends(pegar_sessao)):

    # verificar se o usuário com o mesmo email já existe no banco de dados
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return { "message": "Usuário já existe!" }
        # ja existe algum usuario
    else: 
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        # vai salvar o usuario
        session.commit()
        return { "message": "Usuário criado com sucesso!"}

    