import requests
from urls import Url
import urls


class LoginMethods:
        @staticmethod
        def login_user(body):
            return requests.post(f'{urls.Url.BASE_URL}{urls.URL_user_login}',json=body)


        @staticmethod
        def refresh_token(body):
            return requests.post(f'{urls.Url.BASE_URL}{urls.URL_user_refresh_accessToken}', json=body)


