from random import sample
import pytest

from data import DataForOrderCreate
from generators import generate_user_body


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
def generate_empty_order_data():
    order_body = DataForOrderCreate.CREATE_EMPTY_ORDER_BODY
    return order_body

@pytest.fixture
def generate_order_with_wrong_ingredients():
    order_body = DataForOrderCreate.CREATE_WRONG_ORDER_BODY
    return order_body





