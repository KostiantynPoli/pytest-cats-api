import requests

from src.readEnv import API_URL


class Cat:

    def __init__(self):
        pass

    def get_cats_image(self, api_key, params=None):
        headers = {'x-api-key': api_key,  'Content-Type': 'application/json',}
        response = requests.get(f'{API_URL}/images/search', headers=headers, params=params)
        return response

    def get_cats_breeds(self, params=None):
        headers = {'Content-Type': 'application/json',}
        return requests.get(f'{API_URL}/breeds', headers=headers, params=params)
