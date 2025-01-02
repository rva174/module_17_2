from fastapi import APIRouter
from app.schemas import CreateUser, UpdateUser  # Импортируйте схемы
from app.models import User
from app.backend.db import SessionLocal  # Предполагаем использование сессии БД
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
async def all_tasks():
    pass

@router.get('/task_id')
async def task_by_id():
    pass

@router.post('/create')
async def create_task():
    pass

@router.put('/update')
async def update_task():
    pass

@router.delete('/delete')
async def delete_task():
    pass

