import allure

from methods.login_methods import LoginMethods
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods

class TestGetUserOrders:
    @allure.title ('Успешное получение заказов пользователя при условии пройденной авторизации')
    @allure.description('Получение списка заказов, проверка кода и тела ответа')
    def test_get_user_orders(self, generate_user_data, generate_order_data):
        user = UserMethods.create_user(generate_user_data)
        assert (user.status_code == 200 and user.json()['user']['email'] == generate_user_data['email'])
        response = LoginMethods.login_user(generate_user_data)
        assert response.status_code == 200 and response.json().get("success") is True
        assert "accessToken" in response.json()
        access_token = response.json()["accessToken"]
        order_body = OrderMethods.create_order(generate_order_data)
        assert order_body.status_code == 200 and 'number' in order_body.json()['order']
        user_order = OrderMethods.get_user_orders(generate_order_data,  access_token)
        assert user_order.status_code == 200
        assert user_order.json()['success'] is True
        assert len(user_order.json().get("orders", [])) > 0.


    @allure.title('Успешное получение заказов пользователя без авторизации')
    @allure.description('Ошибка получения списка заказов, проверка кода и тела ответа')
    def test_get_user_orders_without_login(self):
        response = OrderMethods.get_user_orders_without_auth()
        assert response.status_code == 401
        assert response.json() == {"success": False, "message": "You should be authorised"}

