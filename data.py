from order_data import OrderData

class DataForUser:
    CREATE_USER_BODY = {
    "email": "test-data@yandex.ru",
    "password": "password",
    "name": "Username"
    }
    CREATE_LOGOUT_USER_BODY= {
        "token": "{{refreshToken}}"
    }
    CREATE_REFRESH_ACCESSTOKEN_BODY= { # refreshToken который получен после авторизации
        "token": "{{refreshToken}}"
    }
    data_with_wrong_email = {
    "email": "te@yandex.ru",
    "password": "password",
    "name": "Username"
    }
    data_with_wrong_password = {
    "email": "test-data@yandex.ru",
    "password": "passw258ord",
    "name": "Username"
    }


class DataForOrderCreate:
    CREATE_ORDER_BODY = {
        "ingredients": OrderData.get_all_ids()
    }
    CREATE_EMPTY_ORDER_BODY = {
        "ingredients": []
    }
    CREATE_WRONG_ORDER_BODY = {
        "ingredients": ['hfhsjdfj125', 'jfjfjj445']
    }


class ServerReplyMessages:
    user_already_used_error_message =  "User already exists"
    empty_field_error_message = "Email, password and name are required fields"
    wrong_login_and_password_message = "email or password are incorrect"
    update_user_without_auth_message = "You should be authorised"
    empty_ingredients_order_error_message = "Ingredient ids must be provided"


