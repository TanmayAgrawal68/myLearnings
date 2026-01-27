from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    role: Union[str, None] = None


app = FastAPI()

users = []


@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI applicationssssss!"}


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user


@app.get("/users/")
async def list_users():
    if len(users) == 0:
        return {"message": "No users found"}
    return users
