from fastapi import FastAPI
from starlette import status

from fast_zero.schemas import (
    UserSchema,
    UserPublic,
    UserList,
    UpdateUser,
)

app = FastAPI()


@app.post(
    "/users/", status_code=status.HTTP_201_CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    return user


@app.get("/users/", status_code=status.HTTP_200_OK, response_model=UserList)
def list_users():
    return {"users": []}


@app.put(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserPublic,
)
def update_user(user_id: int, user: UpdateUser):
    return user
