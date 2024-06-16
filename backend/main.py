from fastapi import FastAPI
from database.database import engine
import models.produto
from routes.routes_produto import router

models.produto.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)