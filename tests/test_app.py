from fastapi.testclient import TestClient
from starlette import status

from fast_zero.app import app


def test_read_root_must_return_hello_world_and_status_code_200():
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello, World!"}


def test_create_user_must_return_user_and_status_code_201():
    client = TestClient(app)

    user_data = {
        "username": "John Doe",
        "email": "john.doe@test.com",
        "password": "secret",
    }

    response = client.post("/users/", json=user_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "username": "John Doe",
        "email": "john.doe@test.com",
    }
