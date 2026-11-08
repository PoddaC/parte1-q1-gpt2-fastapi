from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routers import generation
from app.services.generation_service import get_generator


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_generator()  # startup: carrega o modelo uma única vez; as requisições o reutilizam
    yield


app = FastAPI(
    title="API de Geração de Texto (GPT-2)",
    description="Recebe uma frase em JSON e devolve uma continuação gerada pelo GPT-2.",
    version="1.0.0",
    lifespan=lifespan,
)
app.include_router(generation.router)
