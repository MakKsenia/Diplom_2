import allure
from methods.user_methods import UserMethods
from data import ServerReplyMessages

@allure.title('Test Successfull user creation')
class TestCreateCourier:
    @allure.title ('Успешное создание пользователя')
    @allure.description('Создание пользователя, проверка кода и тела ответа')
    def test_success_create_user(self, generate_user_data):
        user = UserMethods.create_user(generate_user_data)
        response_body = user.json()
        assert user.status_code == 200 and user.json()['user']['email'] == generate_user_data['email']

    @allure.title ('Невозможность создания пользователя, который уже зарегистрирован')
    @allure.description('Ошибка создания пользователя, проверка кода и тела ответа')
    def test_success_create_same_user_1(self,create_user, generate_user_data):
        # Пытаемся создать второго пользователя с теми же данными
        user2 = UserMethods.create_user(generate_user_data)
        # Проверяем, что создание второго курьера не удалось
        user_already_used_error_message = ServerReplyMessages.user_already_used_error_message
        assert user2.status_code == 403 and user2.json() == {"success": False,
                                                             "message": user_already_used_error_message}


    @allure.title('Невозможность создания пользователя, при оставлении одного из обязательных полей незаполненным')
    @allure.description('Проверяем, что возвращает ошибку, если одного из полей нет')
    def test_failure_create_user_missing_field(self,generate_incomplete_data):
        user = UserMethods.create_user(generate_incomplete_data)
        empty_field_error_message= ServerReplyMessages.empty_field_error_message
        assert user.status_code == 403 and user.json() == {"success": False, "message": empty_field_error_message}
