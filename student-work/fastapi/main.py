import asyncio
from fastapi import Depends, FastAPI, HTTPException, Header, status, Request
from database.base import init_models
from database.models import *
from routes.user import router as user_router
from routes.shops import router as shop_router
from routes.products import router as products_router
import uvicorn



app = FastAPI()
app.include_router(user_router)
app.include_router(products_router)
app.include_router(shop_router)


if  __name__ == "__main__":
    #* Генерация таблиц выполняется запуском файла main.py, а не сервера
    asyncio.run(init_models())
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)