from fastapi import FastAPI
from starlette import status

from fast_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK, response_model=Message)
def read_root():
    return {"message": "Hello, World!"}


@app.post(
    "/users/", status_code=status.HTTP_201_CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    return user
