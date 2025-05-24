import allure

from methods.login_methods import LoginMethods
from data import DataForUser
from data import ServerReplyMessages
from methods.user_methods import UserMethods


class TestLoginUser:
    @allure.title('Успешная авторизация пользователя')
    @allure.description('Проверка возможности курьера авторизоваться с существующими email,password,access_token ')
    def test_success_login_user(self, generate_user_data):
        user = UserMethods.create_user(generate_user_data)
        assert (user.status_code == 200 and user.json()['user']['email'] == generate_user_data['email'])
        response = LoginMethods.login_user(generate_user_data)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()


    @allure.title('Ошибка авторизации пользователя с несуществующим логином - email')
    def test_login_courier_with_wrong_email(self):
        user = LoginMethods.login_user(DataForUser.data_with_wrong_email)
        wrong_login_and_password_message= ServerReplyMessages.wrong_login_and_password_message
        assert user.status_code == 401 and user.json() == {"success": False, "message": wrong_login_and_password_message}

    @allure.title('Ошибка авторизации пользователя с неверным паролем')
    def test_login_with_wrong_password(self):
        user = LoginMethods.login_user(DataForUser.data_with_wrong_password)
        wrong_login_and_password_message = ServerReplyMessages.wrong_login_and_password_message
        assert user.status_code == 401 and user.json() == {"success": False, "message": wrong_login_and_password_message}



