import requests
import data

class UserMethods:
    @staticmethod
    def create_user(body):
        return requests.post(f'{data.Url.BASE_URL}{data.Url.URL_user_create}', json=body)


    @staticmethod
    def logout_user(refreshToken):
        headers = {'Authorization': {refreshToken}}
        return requests.post(f'{data.Url.BASE_URL}{data.URL_user_logout}', headers=headers)

    @staticmethod
    def delete_user(body):
        return requests.delete(f'{data.Url.BASE_URL}{data.Url.URL_user_delete}', json=body)


    @staticmethod
    def update_user(body):
        return requests.patch(f'{data.Url.BASE_URL}{data.Url.URL_user_update}',json=body)
