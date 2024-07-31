from starlette import status


def test_create_user_must_return_user_and_status_code_201(client):
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


def test_list_user_must_return_all_users_and_status_code_200(client):
    response = client.get("/users/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"users": []}


def test_update_user_must_return_user_and_status_code_200(client):
    user_data = {
        "username": "John Doe",
        "email": "john.doe.new@test.com",
    }

    response = client.put("/users/1", json=user_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == user_data
