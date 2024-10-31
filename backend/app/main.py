from fastapi import FastAPI
from backend.app.api.api_main import api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}