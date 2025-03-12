from fastapi import FastAPI
from enum import Enum

app=FastAPI( )

# sample requests and queries
@app.get("/")
async def root() :
    return {"message" : "Hello World"}

# sample path paramters => entries in URL
@app.get("/hello/{name}")
async def say_hello(name: str) :
    return {"message" : f"Hello {name}"}

# Path parameters predefined values
# https://fastapi.tiangolo.com/tutorial/path-params/
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/v1/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

# query parametres are added as elements to the url e.g. items?skip=10&limit=3
# https://fastapi.tiangolo.com/tutorial/query-params/
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/v2/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# Optional parameters added to query, one of the element in Union
from typing import Union

#In this case, there are 3 query parameters:
# needy, a required str.
# skip, an int with a default value of 0.
# limit, an optional int.

@app.get("/v3/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# if you want to send it as a request body you have to define the class inheritet from pydantic base model
# Request Body
# https://fastapi.tiangolo.com/tutorial/body/
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
# create model
@app.post("/v4/items/")
async def create_item(item: Item):
    return item
# using model

@app.post("/v5/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# all together

@app.put("/v6/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# If the parameter is also declared in the path, it will be used as a path parameter.
# If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
# If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.

# additional status code:
# https://fastapi.tiangolo.com/advanced/additional-status-codes/

from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}

@app.put("/v7/items/{item_id}")
async def upsert_item(
    item_id: str,
    name: Union[str, None] = Body(default=None),
    size: Union[int, None] = Body(default=None),
):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)

@app.delete("/v8/items/delete")
async def delete_and_error(error :int):
    return_content = ""
    if error >= 400 and error < 500 :
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=return_content)
    elif error >= 500 and error <600:
        return JSONResponse(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, content=return_content)
    else:
        return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content=return_content)


class Value(str, Enum):
    positive = "positive"
    negative = "negative"


polls_db = {
    1:
    {
        "name": "ARE VOLCANOES COOL?",
        "votes": {
            1:
            {"value": Value.positive},
            2:
            {"value": Value.positive},
            3:
            {"value": Value.positive}
        }
    },
    2: 
    {
        "name": "IS IT 2025?",
        "votes": [
            {"value": Value.positive},
            {"value": Value.negative},
            {"value": Value.positive},
            {"value": Value.negative}
        ]
    }
}

# get all polls
@app.get("/poll")
async def get_all_polls():
    return polls_db

# get specific poll
@app.get("/poll/{poll_id}")
async def get_poll(poll_id: int):
    if poll_id in polls_db:
        return JSONResponse(status_code=status.HTTP_200_OK, content=polls_db[poll_id])
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "poll does not exist"})
    
# get all votes
@app.get("/poll/{poll_id}/vote")
async def get_all_votes_from_poll(poll_id: int):
    if poll_id in polls_db:
        return JSONResponse(status_code=status.HTTP_200_OK, content=polls_db[poll_id]["votes"])
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "poll does not exist"})

# get specific vote
@app.get("/poll/{poll_id}/vote/{vote_id}")
async def get_vote_from_poll(poll_id: int, vote_id: int):
    if poll_id in polls_db:
        if vote_id in polls_db[poll_id]["votes"]:
            return JSONResponse(status_code=status.HTTP_200_OK, content=polls_db[poll_id]["votes"][vote_id])
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "vote does not exist"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "poll does not exist"})
    


# create a new poll
@app.post("/poll")
async def create_poll(
    poll_id: int,
    name: Union[str, None] = Body(default=None),
):
    if poll_id in polls_db:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "poll of a given id already exists"})
    polls_db.update({poll_id: {"name": name, "votes": dict()}})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message" : "poll has been successfully created", "polls": polls_db})

# create a new vote
@app.post("/poll/{poll_id}/vote")
async def create_vote_for_poll(poll_id: int, vote_id: int, vote_value: str):
    if poll_id not in polls_db:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "poll does not exist"})

    polls_db[poll_id]["votes"].update({vote_id: {"value": vote_value}})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "vote has been successfully created", "polls": polls_db})
    

# modify a poll
@app.put("/poll/{poll_id}")
async def update_poll(poll_id: int, name: str):
    if poll_id in polls_db:
        polls_db[poll_id]["name"] = name
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message" : "poll has been successfully changed", "polls": polls_db})   
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "poll does not exist"})

# modify a vote
@app.put("/poll/{poll_id}/vote/{vote_id}")
async def update_vote_for_poll(poll_id: int, vote_id: int, vote_value: str):
    if poll_id in polls_db:
        if vote_id in polls_db[poll_id]["votes"]:
            polls_db[poll_id]["votes"][vote_id]["value"] = vote_value
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "vote has been successfully changed", "polls": polls_db})
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "vote does not exist"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "poll does not exist"})


# delete a poll
@app.delete("/poll/{poll_id}")
async def delete_poll(poll_id: int):
    if poll_id in polls_db:
        del polls_db[poll_id]
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "poll has been successfully deleted", "polls": polls_db})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "poll does not exist"})

# delete a vote
@app.delete("/poll/{poll_id}/vote/{vote_id}")
async def delete_vote_from_poll(poll_id: int, vote_id: int):
    if poll_id in polls_db:
        if vote_id in polls_db[poll_id]["votes"]:
            del polls_db[poll_id]["votes"][vote_id]
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "vote has been successfully deleted", "polls": polls_db})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message" : "poll does not exist"})   