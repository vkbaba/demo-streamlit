from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

items = {}  # アイテムを保存するための辞書
id_counter = 0  # IDジェネレータ

@app.post("/items/")
def create_item(item: Item):
    global id_counter
    item_id = id_counter
    id_counter += 1
    # 作成されるアイテムにidを設定
    stored_item = item.dict()
    stored_item["id"] = item_id
    items[item_id] = stored_item
    return stored_item

@app.get("/items/{item_id}")
def read_item(item_id: int):  # item_idを整数型として受け取る
    item = items.get(item_id)
    if item:
        return item
    else:
        return {"error": "Item not found"}

@app.get("/items/")
def read_items():
    return list(items.values())