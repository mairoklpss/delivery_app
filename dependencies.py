from models import db
from sqlalchemy.orm import sessionmaker

#cada alteração no banco de dados precisa ser feita dentro de uma sessão aberta.
def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    # com finally vai executar indepedentemente se deu certo ou não, vai fechar a sessão.
    finally:
        session.close()
