from fastapi import FastAPI
from pydantic import BaseModel, Field 
from uuid import UUID

class Book(BaseModel):
    id: UUID
    title: str=Field(min_length=1,max_length=100)
    author: str=Field(min_length=1,max_length=100)
    description: str=Field(min_length=1, max_length=100)
    rating : float=Field(gt=-1.0, lt=10.0)

Books=[]


app=FastAPI()
@app.get('/')
async def hello():
    return Books

@app.post('/')
async def createBook(book:Book):
    Books.append(book)
    return book