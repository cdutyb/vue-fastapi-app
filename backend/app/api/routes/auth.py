from fastapi import APIRouter

auth_router = APIRouter()

#auth模块实现 用户注册 登录 退出等功能
@auth_router.get("/login")
def login():
    return {"message": "Login"}