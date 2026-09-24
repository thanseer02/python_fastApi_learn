from fastapi import FastAPI, HTTPException
import items as it

from pandas_ln import get_data_panda

app = FastAPI()

CSV_FILE = "items.csv"


@app.get("/")
def root():
    return {"Hello": "world"}


@app.get("/item")
def getItems():
    items = it.load_data()
    return items

@app.get("/pd")
def pandas_data():
    result = get_data_panda()
    return result

@app.post("/item")
def create_item(item: str):
    items = it.load_data()
    items.append(item)
    it.write_all_items(items)
    return item


@app.get("/item/{item_id}")
def get_item(item_id: int):
    return it.load_data(item_id)


@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    items =it.load_data()

    if item_id < 0 or item_id >= len(items):
        raise HTTPException(
            status_code=404,
            detail="There is no item"
        )

    deleted_item = items.pop(item_id)
    it.write_all_items(items)

    return {
        "message": "Item deleted",
        "item": deleted_item
    }


@app.put("/item/{item_id}")
def update_item(item_id: int, item: str):
    items =  it.load_data()

    if item_id < 0 or item_id >= len(items):
        raise HTTPException(
            status_code=404,
            detail="There is no item"
        )

    old_item = items[item_id]
    items[item_id] = item

    it.write_all_items(items)

    return {
        "message": "Item updated",
        "old_item": old_item,
        "new_item": item
    }


@app.get("/pd")
def pandas_data():
    result = get_data_panda()
    return result

