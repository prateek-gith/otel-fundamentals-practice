from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.telemetry import setup_telemetry
from app.routers.users import router
from prometheus_fastapi_instrumentator import Instrumentator



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
Instrumentator().instrument(app).expose(app)


@app.get("/")
def home():
    return {
        "message": "FastAPI OpenTelemetry App Running"
    }
