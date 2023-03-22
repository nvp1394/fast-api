from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated 
from typing import Dict, Any
import uvicorn
import json

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Two'},
    'book_5': {'title': 'Title Five', 'author': 'Author Two'},
}

@app.get("/books/{author_name}")
async def get_books(author_name: str):
    books = []
    for book, value in BOOKS.items():
        if value.get("author").lower() == author_name.lower():
            books.append(value)
    if books:
        return {"Status": "Success", 
                "Code": 200, 
                "Body": books}
    else:
        return {"Status": "Success", 
                "Code": 200, 
                "Body": "No books found"}

@app.put("/update_book/")
async def update_author(update_authorName = Body(default="Dictionary")):
    update = False
    for book, value in BOOKS.items():
        if value.get('title').lower() == update_authorName.get('title').lower():
            BOOKS[book] = update_authorName
            update = True
            break
    if update:
        return {"Status": "Success", 
                "Code": 200, 
                "Body": BOOKS}
    else:
        return {"Status": "Unsuccessful"}
    
if __name__ =="__main__":
    uvicorn.run("practice1:app",host="0.0.0.0", reload=True)