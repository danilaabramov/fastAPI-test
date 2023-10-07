from fastapi import FastAPI, Query, Path

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


users = [
    {
        
    }
]