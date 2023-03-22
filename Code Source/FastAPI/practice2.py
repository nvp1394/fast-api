from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
import uvicorn
from typing import Optional

app = FastAPI()

#Field is for extra validation for our columns to gets input as expected.

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1) # minimum length of title should be one
    author: str = Field(min_length=1, max_length=100) # minium length of author should be 1 and Max should be 100
    descripiton: Optional[str] = Field(title="Description of the book", 
                             max_length=100, 
                             min_length=1) # description
    rating: int = Field(gt=-1, lt=101) # clients rating should be between 0-100 gt = greater then, lt = less then
    class Config:
        schema_extra = {
            "example": {
                "id":"ea5209b0-818c-4519-989b-0f10d8081a39",
                "title": "Computer Science Pro",
                "author": "learning with Rody",
                "description": "A very nyc descripition of the book",
                "rating": 100
            }
        }

BOOKS = []

@app.get('/book')
async def read_all_books(books_to_return: Optional[int] = None):
    if not BOOKS:
        create_books_no_api()
    if books_to_return and len(BOOKS)>=books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i +=1
        return new_books
    return BOOKS


@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return BOOKS

@app.get("/book/{book_id}")
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.put("/{book_id}")
async def update_book(bookd_id: UUID, book:Book):
    for index,b in enumerate(BOOKS):
        if b.id == bookd_id:
            BOOKS[index] = book
            return BOOKS


@app.delete("/book/{delete_book_id}")
async def delete_book(delete_book_id: UUID, book:Book):
    for index, b in enumerate(BOOKS):
        if b.id == delete_book_id:
            BOOKS.pop(index)
            return BOOKS







def create_books_no_api():
    book1 = Book(id="ea5209b0-818c-4519-989b-0f10d8081a19",
                 title = "Title 1", 
                 author= "Author 1", 
                 descripiton="Descripton 1",
                 rating= 60)
    book2 = Book(id="ea5209b0-818c-4519-989b-0f10d8081a29",
                 title = "Title 2", 
                 author= "Author 3", 
                 descripiton="Descripton 2",
                 rating= 70)
    book3 = Book(id="ea5209b0-818c-4519-989b-0f10d8081a39",
                 title = "Title 3", 
                 author= "Author 3", 
                 descripiton="Descripton 3",
                 rating= 80)
    book4 = Book(id="ea5209b0-818c-4519-989b-0f10d8081a39",
                 title = "Title 4", 
                 author= "Author 4", 
                 descripiton="Descripton 4",
                 rating= 90)
    
    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)

if __name__ == "__main__":
    uvicorn.run("practice2:app", reload=True)