from fastapi import FastAPI
from .api import api_v1_router, Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router=api_v1_router, prefix="/api/v1")


@app.get("/")
def index():
    return "Documentation: http://127.0.0.1:8000/docs"
