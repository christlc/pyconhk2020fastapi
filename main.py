from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


local_dict = {}


@app.get("/messages/")
def list_items():
    return local_dict


@app.get("/messages/{item_id}")
def read_item(item_id: int):
    return {item_id: local_dict.get(item_id)}


@app.post("/messages/{item_id}")
def post_item(item_id: int, message: str):
    local_dict[item_id] = message


from schema import Message


@app.post("/messages/body/{item_id}")
def post_item_json(item_id: int, message: Message):
    local_dict[item_id] = message


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", workers=1)
