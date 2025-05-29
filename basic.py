from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field 
from uuid import UUID

class Book(BaseModel):
    id: UUID
    title: str=Field(min_length=1,max_length=100)
    author: str=Field(min_length=1,max_length=100)
    description: str=Field(min_length=1, max_length=100)
    rating : float=Field(gt=-1.0, lt=10.0)

#empty list of books
Books=[]
app=FastAPI()


@app.get('/')
async def start():
    return Books

#creates books
@app.post('/')
async def createBook(book:Book):
    Books.append(book)
    return book

#update those books in the Books list
@app.put('/{bookID}')
async def updateBook(bookID:UUID,book:Book):
    ctr=0
    for x in Books:
        ctr+=1
        if x.id==bookID:
            Books[ctr-1]=book 
            return Books[ctr-1]
    raise HTTPException(status_code=404, detail=f"book id {bookID} does not exist")


#delete the books
@app.delete('/{bookID}')
async def deleteBook(bookID:UUID):
    ctr=0
    for x in Books:
        ctr+=1
        if x.id==bookID:
            del Books[ctr-1]
            return f"ID {bookID} has been deleted"
    raise HTTPException(status_code=404, detail=f"{bookID} has been deleted")