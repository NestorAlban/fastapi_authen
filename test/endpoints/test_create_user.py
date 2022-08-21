import pytest
from app.usercase import UserCreator
from app.schemas import UserInfoBack
from app.database import DataBase
from app.models import User
from app.database import DataBase
from app.services import UserService
EXAMPLE_NAME = "Example"
from fastapi.testclient import TestClient


def test_create_user_endpoint(app):
    client = TestClient(app)
    response = client.post(
        "/create_user",
        json={
            "name": EXAMPLE_NAME,
            "email": "example_email",
            "password": "example_password",
        }

    ).json()
    print(response)  
    assert response  # db.session.delete(user)
    assert response.get('name') == EXAMPLE_NAME

