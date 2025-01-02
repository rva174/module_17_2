from fastapi import FastAPI

from sqlalchemy.schema import CreateTable
from app.backend.db import engine, Base
from app.models import User
from app.models import Task

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Печать SQL запросов на создание таблиц
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# app.include_router(user.router)
# app.include_router(task.router)


