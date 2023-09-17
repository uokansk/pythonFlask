# Задание №6
# 📌 Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс User с полями id, name, email и password.
# 📌 Создайте список users для хранения пользователей.
# 📌 Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# 📌 Создайте маршрут для отображения списка пользователей (метод GET).
# 📌 Реализуйте вывод списка пользователей через шаблонизатор Jinja.

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class UserOut(BaseModel):
    id: int
    name: str
    email: str


class UserIn(BaseModel):
    name: str
    email: str
    password: int


class User(UserIn):
    id: int


users = []
for i in range(10):
    users.append(User(
        id=i + 1,
        name=f'name{i + 1}',
        email=f'email{i + 1}@mail.ru',
        password=123 + i,
    ))


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.post("/users/", response_model=User)
async def create_users(new_user: UserIn):
    users.append(User(id=len(users) + 1,
                      name=new_user.name,
                      email=new_user.email,
                      password=new_user.password))
    return users[-1]


@app.put("/users/{users_id}")
async def update_users(id: int, user: User):
    return {"id": id, "user": user}


@app.put("/users/", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    for i in range(0, len(users)):
        if users[i].id == user_id:
            current_user = users[user_id - 1]
            current_user.name = new_user.name
            current_user.email = new_user.email
            current_user.password = new_user.password
            return current_user
        raise HTTPException(status_code=404, detail="user not found")


@app.delete("/users/", response_class=HTMLResponse)
async def delete_user(request: Request, user_id: int):
    for user in users:
        if users[i].id == user_id:
            users.remove(user)
            break
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


if __name__ == '__main__':
    uvicorn.run(
        "main_06:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
