import allure

from methods.login_methods import LoginMethods
from data import ServerReplyMessages
from methods.user_methods import UserMethods


class TestUpdateUser:
    @allure.title('Успешное изменение всех полей данных пользователя')
    @allure.description('Проверка возможности изменения данных пользователя')
    def test_update_user(self, generate_user_data, generate_update_user_data):
        user = UserMethods.create_user(generate_user_data)
        assert (user.status_code == 200 and user.json()['user']['email'] == generate_user_data['email'])
        response = LoginMethods.login_user(generate_user_data)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()
        user_update = UserMethods.update_user(generate_update_user_data)
        assert user_update.status_code == 200 and user_update.json()['user']['email'] == generate_update_user_data['email'] and ['user']['name'] == generate_update_user_data['name']


    @allure.title('Невозможность изменить данные пользователя, не пройдя авторизацию')
    @allure.description('Невозможность изменить данные пользователя, не пройдя авторизацию')
    def test_update_user_without_auth(self,generate_user_data, generate_update_user_data):
        user = UserMethods.create_user(generate_user_data)
        assert user.status_code == 200 and user.json()['user']['email'] == generate_user_data['email']
        user = UserMethods.update_user(generate_update_user_data)
        update_user_without_auth_message= ServerReplyMessages.update_user_without_auth_message
        assert user.status_code == 401 and user.json() == {"success": False, "message": update_user_without_auth_message}