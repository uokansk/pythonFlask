# Задание №3
# 📌 Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс User с полями id, name, email и password.
# 📌 Создайте список users для хранения пользователей.
# 📌 Создайте маршрут для добавления нового пользователя (метод POST).
# 📌 Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
