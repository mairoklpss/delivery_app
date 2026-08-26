from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

#cria a conexão com o banco de dados
db = create_engine("sqlite:///banco.db")

#base do banco de dados
Base = declarative_base()

#criar as classes/tabelas do banco de dados
# Usuario
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)# se é admin ou apenas um usuario comum

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Pedido  
class Pedido(Base):
    __tablename__ = "pedidos"

    #status padrao dos pedidos
    # STATUS_PEDIDOS = (
    #     #(chave, valor)
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True) 
    #ChoiceType(choices=STATUS_PEDIDOS)
    status = Column("status", String) # pendente, cancelado, finalizado 
    usuario = Column("usuario", Integer, ForeignKey("usuarios.id")) # id do usuario que fez o pedido
    preco = Column("preco", Float)

    def __init__(self, usuario, status="PENDENTE", preco=0.0):
        self.status = status
        self.usuario = usuario
        self.preco = preco

        
# ItensPedido
class ItensPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", Integer, ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#executa a criação dos metadados no banco de dados
