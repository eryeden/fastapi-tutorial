from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel


app = FastAPI()


# root
@app.get("/")
async def root():
    return {"message": "Hello World"}


# path parameter
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# path parameter with type
@app.get("/int_items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# path operations
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


# path operations with user ID
@app.get("/users/{user_id}")
async def read_user_id(user_id: str):
    return {"user_id": user_id}


# Enum version of the path parameter
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):  # API request parameter is forced to be Enum using Type hint.
    if model_name is ModelName.alexnet:
        return {"model_name": model_name,
                "message": "Alexnet is detected using Enum."}

    if model_name.value == "lenet":
        return {"model_name": model_name,
                "message": "Lenet is detected using its value."}

    return {"model_name": model_name,
            "message": "Default return."}


# File path support of URL parameter on FastAPI
# but OpenAPI does not support file path like parameter due to the confusion of API.
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Query parameters, which is a parameter appended to URL like /home/user/?room=0&status=open
# You can test by following URL:
# http://127.0.0.1:8000/items/query/?skip=20&limit=1000
@app.get("/items/query/")
async def read_item_by_query_parameters(skip: int = 0, limit: int = 10):
    return {"message": "this is a test of query parameter",
            "skip": skip,
            "limit": limit}


# Request body
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.post("/items/request_body/")
async def create_item(item: Item):
    return item


