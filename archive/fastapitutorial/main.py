from fastapi import FastAPI, HTTPException

from models import Item

app = FastAPI()


items: list[Item] = [
    Item(id=1, name="foo", description="demo item 1", stock=1),
    Item(id=2, name="bar", description="demo item 2", stock=10),
]


@app.get("/")
def status() -> dict:
    return {"status": "ok"}


@app.get("/items")
def get_all_items() -> list[Item]:
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item with id: {item_id} could not be found")


@app.post("/items")
def create_item(item: Item) -> Item:
    for i in items:
        if item.id == i.id:
            raise HTTPException(status_code=400, detail=f"Item with id: {item.id} already exists")
    items.append(item)
    return item


@app.put("/items")
def update_item(item: Item) -> Item:
    for i in items:
        if i.id == item.id:
            i.name = item.name
            i.stock = item.stock
            i.description = item.description
            return i
    raise HTTPException(status_code=404, detail=f"Item with id: {item.id} could not be found")


@app.delete("/items/{item_id}")
def delete_item(item_id: str) -> None:
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return None
    raise HTTPException(status_code=400, detail=f"Item with id: {item_id} doesn't exist")
