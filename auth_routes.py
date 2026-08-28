from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context

from schemas import UsuarioSchema
from schemas import LoginSchema
from sqlalchemy.orm import Session

# roteador para autenticação
# prefixo: caminho da rota, tags: subtitulo da documentação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(id):
    token = f"fgabbfadnoiieourgbuer9hviq{id}"
    return token

def autenticacao(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()

    return usuario

@auth_router.get('/')
async def home():
    """
    Essa é a rota de autenticação
    """
    return {
        "message": "Você acessou a rota de autenticação"
    }


# FUNÇÃO DE CRIAR CONTA
@auth_router.post('/criar_conta')
#função de criar conta, recebe email e senha como parâmetros e ambos sao STRING
async def criar_conta(usuario_schema: UsuarioSchema, session: Session=Depends(pegar_sessao)):

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

# FUNÇÃO DE LOGIN
# login -> email e senha -> token JWT
@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    # verificar se o usuário com o mesmo email já existe no banco de dados
    usuario = session.query(Usuario).filter(Usuario.email == login_schema.email).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="E-mail ou senha inválidos")
    # se o usuario existir, a api retorna um token JWT
    else:
        access_token = criar_token(usuario.id)
        return {"access_token": access_token, "token_type": "Bearer"}