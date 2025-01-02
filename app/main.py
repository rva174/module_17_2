from fastapi import FastAPI
from sqlalchemy.schema import CreateTable
from app.backend.db import engine, Base

from app.models import User
from app.models import Task
from app.routers import user_router, task_router

app = FastAPI()

# Создание таблиц
#Base.metadata.create_all(bind=engine)

# Печать SQL запросов
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user_router)
app.include_router(task_router)


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host='0.0.0.0', port=8000)