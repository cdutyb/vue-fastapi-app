from fastapi import APIRouter

data_router = APIRouter()


@data_router.get("/info")
def get_data():
    return {"message": "Data Info"}