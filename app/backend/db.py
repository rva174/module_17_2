# В модуле db.py:
# Импортируйте все необходимые функции и классы , создайте движок указав пусть в БД
# 'sqlite:///taskmanager.db' и локальную сессию (по аналогии с видео лекцией).
# Создайте базовый класс Base для других моделей, наследуясь от DeclarativeBase.




from sglalchemy import create_engine
from sglalchemy.orm import sessionmaker, DeclarativeBase
from sglalchemy import Column, Integer, String




engine = create_engine("sqlite:///taskmanager.db")

class Base(DeclarativeBase):
    pass