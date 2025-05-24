import requests
import data


class LoginMethods:
        @staticmethod
        def login_user(body):
            return requests.post(f'{data.Url.BASE_URL}{data.Url.URL_user_login}',json=body)


        @staticmethod
        def refresh_token(body):
            return requests.post(f'{data.Url.BASE_URL}{data.URL_user_refresh_accessToken}', json=body)


