
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os

app = FastAPI(title="Tarea 2 - FastAPI", version="1.0.0")

class Item(BaseModel):
    id: int
    name: str
    price: float

DB: List[Item] = [
    Item(id=1, name="Notebook", price=15.5),
    Item(id=2, name="Pen", price=2.0),
]

@app.get("/", summary="Welcome")
def root():
    return {
        "message": "Bienvenido a la API de FastAPI para la Tarea 2 (Multi-Stage Build)",
        "docs": "/docs",
        "health": "/api/health"
    }

@app.get("/api/health", summary="Healthcheck")
def health():
    return {"status": "ok"}

@app.get("/api/items", response_model=List[Item], summary="List items")
def list_items():
    return DB

@app.post("/api/items", response_model=Item, summary="Create item")
def create_item(item: Item):
    if any(x.id == item.id for x in DB):
        raise HTTPException(status_code=409, detail="Item with this ID already exists")
    DB.append(item)
    return item

# Nota: el puerto lo define uvicorn al ejecutar.
PORT = int(os.getenv("PORT", "8000"))
