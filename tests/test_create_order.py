import allure

from methods.login_methods import LoginMethods
from methods.order_methods import OrderMethods
from conftest import generate_order_data
from methods.user_methods import UserMethods
from data import ServerReplyMessages

class TestCreateOrder:
    @allure.title('Успешное создание заказа без авторизации пользователя')
    @allure.description('Проверка создания заказа с корректными данными')
    def test_create_order_with_correct_data_without_login(self, generate_order_data):
        order_body = OrderMethods.create_order(generate_order_data)
        assert order_body.status_code == 401

    @allure.title('Успешное создание заказа после авторизации пользователя')
    @allure.description('Проверка создания заказа с корректными данными авторизованным пользователем')
    def test_create_order_with_correct_data(self, generate_order_data, generate_user_data):
        user = UserMethods.create_user(generate_user_data)
        assert (user.status_code == 200 and user.json()['user']['email'] == generate_user_data['email'])
        response = LoginMethods.login_user(generate_user_data)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()
        order_body = OrderMethods.create_order(generate_order_data)
        assert order_body.status_code == 200 and 'number' in order_body.json()['order']

    @allure.title('Ошибка при создании заказа без ингредиентов')
    @allure.description('Проверка создания заказа с пустыми ингедиентами')
    def test_create_order_with_empty_ingredients(self, generate_empty_order_data):
        order_body = OrderMethods.create_order(generate_empty_order_data)
        empty_ingredients_order_error_message = ServerReplyMessages.empty_ingredients_order_error_message
        assert order_body.status_code == 400 and order_body.json() == {"success": False,"message": empty_ingredients_order_error_message}

    @allure.title('Ошибка при создании заказов с неверным хэшем (id) ингредиентов')
    @allure.description('Проверка создания заказа с несуществующими ингедиентами')
    def test_create_order_with_wrong_ingredients(self, generate_order_with_wrong_ingredients):
        order_body = OrderMethods.create_order(generate_order_with_wrong_ingredients)
        assert order_body.status_code == 500