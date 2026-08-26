from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

# para rodar o código: uvicorn main:app --reload
app = FastAPI()

# criar um contexto de criptografia para senhas
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# importar as rotas
from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
