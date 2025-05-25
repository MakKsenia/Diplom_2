from random import sample
import pytest

from data import DataForOrderCreate
from generators import generate_user_body
from methods.user_methods import UserMethods


@pytest.fixture
def generate_user_data():
    user_body = generate_user_body()
    email = user_body["email"]
    password = user_body["password"]
    name = user_body["name"]
    return user_body


@pytest.fixture
def generate_incomplete_data():
    user_body = generate_user_body()
    user_body['email'] = ''
    password = user_body['password']
    name = user_body['name']
    return user_body

@pytest.fixture
def generate_update_user_data():
    user_body = generate_user_body()
    email = user_body["email"]
    name = user_body["name"]
    return user_body

@pytest.fixture
def generate_order_data():
    order_body = DataForOrderCreate.CREATE_ORDER_BODY
    order_body["ingredients"] = sample(DataForOrderCreate.CREATE_ORDER_BODY["ingredients"], 2)
    return order_body

@pytest.fixture
def create_user(generate_user_data):
    user = UserMethods.create_user(generate_user_data)
    assert user.status_code == 200 and user.json()['user']['email'] == generate_user_data['email']
    yield user
    UserMethods.delete_user(generate_user_data['email'])







