import datetime
import random
from enum import Enum
from http.client import HTTPException
from typing import List

import databases
import router
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///my_database.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("firstname", sqlalchemy.String(56)),
                         sqlalchemy.Column("lastname", sqlalchemy.String(56)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(128)), )

products = sqlalchemy.Table("products",
                            metadata,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("name_product", sqlalchemy.String(56)),
                            sqlalchemy.Column("description", sqlalchemy.String(128)),
                            sqlalchemy.Column("price", sqlalchemy.Integer), )
orders = sqlalchemy.Table("orders",
                          metadata,
                          sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                          sqlalchemy.Column('user_id', sqlalchemy.ForeignKey("users.id")),
                          sqlalchemy.Column('product_id', sqlalchemy.ForeignKey("products.id")),
                          sqlalchemy.Column("date_order", sqlalchemy.Date),
                          sqlalchemy.Column("order_status", sqlalchemy.String(32)),
                          )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
app = FastAPI()


class UserIn(BaseModel):
    firstname: str = Field(max_length=56)
    lastname: str = Field(max_length=56)
    email: str = Field(max_length=128)
    password: str = Field(max_length=128)


class User(BaseModel):
    id: int
    firstname: str = Field(max_length=56)
    lastname: str = Field(max_length=56)
    email: str = Field(max_length=128)
    password: str = Field(max_length=128)


class Product(BaseModel):
    id: int
    name_product: str = Field(max_length=56)
    description: str = Field(max_length=128)
    price: int


class ProductIn(BaseModel):
    name_product: str = Field(max_length=56)
    description: str = Field(max_length=128)
    price: int


class Status(Enum):
    unpaid = 'Ждёт оплаты'
    paid = 'Оплачен'
    shipped = 'Отгружен'
    cancelled = 'Отменён'
    completed = 'Выполнен'


class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    date_order: datetime.date
    order_status: str = Field(max_length=32)


class OrderIn(BaseModel):
    user_id: int = Field(..., title="User ID")
    product_id: int = Field(..., title="Product ID")
    date_order: datetime.date = Field(..., title="Date")
    order_status: Status = Field(..., title="Status")


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(firstname=f'user{i}',
                                      lastname=f'user_fam{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=f'asd12{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@app.get("/fake_product/{count}")
async def create_note(count: int):
    for i in range(count):
        query = products.insert().values(name_product=f'product{i}',
                                         description=f'product{i}',
                                         price=f'{random.randint(1000, 10000)}',
                                         )
        await database.execute(query)
    return {'message': f'{count} fake_product create'}


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name_product=user.name_product,
                                  lastname=user.lastname,
                                  email=user.email,
                                  password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(name_product=product.name_product,
                                     description=product.description,
                                     price=product.price,
                                     )
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.get("/products/", response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


@app.delete("/products/{product_id}")
async def delete_user(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'product deleted'}


@router.get("/orders/", response_model=list[Order])
async def get_orders():
    query = select(orders.c.id.label('order_id'), orders.c.date.label('order_date'),
                   orders.c.status.label('order_status'),
                   users.c.id.label('user_id'), users.c.first_name.label('user_first_name'),
                   users.c.last_name.label('user_last_name'), users.c.email.label('user_email'),
                   products.c.id.label('product_id'), products.c.title.label('product_title'),
                   products.c.description.label('product_description'), products.c.price.label('product_price')
                   ).join(products).join(users)
    return await database.fetch_all(query)


@router.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    query = select(orders.c.id.label('order_id'), orders.c.date.label('order_date'),
                   orders.c.status.label('order_status'),
                   users.c.id.label('user_id'), users.c.first_name.label('user_first_name'),
                   users.c.last_name.label('user_last_name'), users.c.email.label('user_email'),
                   products.c.id.label('product_id'), products.c.title.label('product_title'),
                   products.c.description.label('product_description'), products.c.price.label('product_price')
                   ).where(orders.c.id == order_id).join(products).join(users)
    fetch = await database.fetch_one(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Order not found')
    return fetch


@router.post("/orders/", response_model=Order)
async def add_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id,
                                   product_id=order.product_id,
                                   date=order.date,
                                   status=order.status)
    last_record_id = await database.execute(query)
    return await get_order(last_record_id)


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Order not found')
    return await get_order(order_id)


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Order not found')
    return {'message': 'Order deleted'}


if __name__ == '__main__':
    uvicorn.run(
        "hworks.hw6.main_06:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
