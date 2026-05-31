from fastapi import FastAPI

from database import engine
from models import Base
from telemetry import setup_telemetry
from routers.users import router

app = FastAPI(
    title="FastAPI OpenTelemetry App"
)

Base.metadata.create_all(
    bind=engine
)

setup_telemetry(
    app,
    engine
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "FastAPI OpenTelemetry App Running"
    }
