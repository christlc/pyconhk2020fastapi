from fastapi import FastAPI
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != 'root' or form_data.password != 'password': # should replace with hashed password
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": 'mytoken', "token_type": "bearer"}


@app.get("/")
def read_root(token: str = Depends(oauth2_scheme)):
    assert token == 'mytoken'
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
    uvicorn.run("main2:app", host="0.0.0.0", port=8001, log_level="info", workers=1)

