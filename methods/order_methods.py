import requests
import urls
from urls import Url

class OrderMethods:
    @staticmethod
    def get_ingredients_info():
        return requests.get(f'{urls.Url.BASE_URL}{urls.Url.URL_get_ingredients}')

    @staticmethod
    def create_order(body):
        return requests.post(f'{urls.Url.BASE_URL}{urls.Url.URL_orders_create}', json=body)

    @staticmethod
    def get_user_orders(body, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            }
        return requests.get(f'{urls.Url.BASE_URL}{urls.Url.URL_get_user_orders}', json=body, headers=headers)

    @staticmethod
    def get_user_orders_without_auth():
        return requests.get(f'{urls.Url.BASE_URL}{urls.Url.URL_get_user_orders}')