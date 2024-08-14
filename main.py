# main.py

from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items