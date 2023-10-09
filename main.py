from pydantic.dataclasses import dataclass
from datetime import datetime
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, Query, Path, APIRouter

app = FastAPI()


@app.get("/")
def ping():
    return "pong"


@app.get(
    path="/hello",
    tags=["hello"],
    name='Печатай "Hello, World!"',
    description='Возвращает типовое приветствие'
)
def print_hello():
    return "Hello, world!"


@app.get('/print/{something}')
def print_something(
        something: int = Path(),
        s: str = Query(
            default='трава', title='строка поиска', min_length=5, max_length=64, deprecated=True,
            examples=['Мир', 'Труд', 'Май', 'Май']
        )
):
    return {'msg': f'Печатаю что-то: {something} {s}'}


@dataclass
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    age: int
    created_at: datetime


users = [
    User(id=1, username='andreq2', first_name='Andrew', last_name='Johns', age=23, created_at=datetime.now()),
    {
        'id': 2,
        'username': 'mart3',
        'first_name': 'Marti',
        'last_name': 'Fletcher',
        'age': 32,
        'created_at': datetime.now()
    },
    {
        'id': 3,
        'username': 'bm32',
        'first_name': 'Billy',
        'last_name': 'Murdack',
        'age': 83,
        'created_at': datetime.now()
    },
]
# POST, GET, DELETE, PUT

user_router = APIRouter(prefix='/users', tags=['Пользователи'])


class UserSchema(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    age: int
    created_at: datetime

    class Config:
        json_schema_extra = {'example': {
            'id': 1,
            'username': 'john1',
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 3,
            'created_at': datetime.now()
        }}


@user_router.get('/', name='Все пользователи', response_model=List[User])
def get_all_users():
    return users


app.include_router(user_router)
