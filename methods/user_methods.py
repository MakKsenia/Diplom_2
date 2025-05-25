import requests
import urls

class UserMethods:
    @staticmethod
    def create_user(body):
        return requests.post(f'{urls.Url.BASE_URL}{urls.Url.URL_user_create}', json=body)


    @staticmethod
    def logout_user(refreshToken):
        headers = {'Authorization': {refreshToken}}
        return requests.post(f'{urls.Url.BASE_URL}{urls.URL_user_logout}', headers=headers)

    @staticmethod
    def delete_user(body):
        return requests.delete(f'{urls.Url.BASE_URL}{urls.Url.URL_user_delete}', json=body)


    @staticmethod
    def update_user(body):
        return requests.patch(f'{urls.Url.BASE_URL}{urls.Url.URL_user_update}',json=body)
