from fastapi import FastAPI
app=FastAPI()
@app.get('/')
async def hello():
    return {"message":"hello!"}

@app.get('/{name}')
async def greet(name:str) -> dict:
    return {"message":f"hello, {name}"}