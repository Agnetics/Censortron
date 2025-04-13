from fastapi import FastAPI
from . import config
from .routes import router

app = FastAPI(
    title="Мое приложение",
    description="Описание приложения",
    version="1.0.0"
)

app.include_router(router)