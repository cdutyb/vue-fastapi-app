from fastapi import APIRouter

data_router = APIRouter()

#data模块实现 数据库读取数据 可视化展示 功能
@data_router.get("/info")
def get_data():
    return {"message": "Data Info"}