from fastapi import FastAPI
# para rodar o código: uvicorn main:app --reload
app = FastAPI()

# importar as rotas
from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)