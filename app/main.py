# from fastapi import FastAPI
# from app.backend.db import Base
# from app.models import task, user

from fastapi import FastAPI
# from app.models.user import user
# from app.models.task import task
from routers.user import user
from routers.task import task




app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

