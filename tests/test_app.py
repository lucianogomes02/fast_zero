from fastapi.testclient import TestClient
from fast_zero.app import app
from starlette import status


def test_read_root_must_return_hello_world_and_status_code_200():
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello, World... again"}
