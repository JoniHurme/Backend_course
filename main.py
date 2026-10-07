from fastapi import FastAPI

app = FastAPI()


books = [
    {"id": 0, "name": "Metro 2033", "author": "Dmitry Glukhovsky"},
    {"id": 1, "name": "Metro 2034", "author": "Dmitry Glukhovsky"},
    {"id": 2, "name": "Kalevala", "author": "Elias Lönnrot"},
    {"id": 3, "name": "Roadside Picnic", "author": "Arkady and Boris Strugatsky"},
    {"id": 4, "name": "The Pragmatic Programmer", "author": "Andrew Hunt and David Thomas"},
    {"id": 5, "name": "The rust book", "author": "Rust Lang"},
]


@app.get("/books")
def get_books():
    return books

app.get("/books/{book_id}")
def get_book_by_id():
    pass

app.get("/books")
def get_book_by_auth(author: str):
    pass
