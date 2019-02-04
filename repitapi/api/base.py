import requests
from rest_framework import status
from requests.compat import urljoin
from repitapi.constants import BASE_URL


class RepitAPI(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _get_request_headers():
        headers = {
            'Accept': 'application/json',
        }
        return headers

    def _request_get(self, path, params=None, json=True, url=BASE_URL):
        url = urljoin(url, path)
        headers = self._get_request_headers()
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        if json:
            return response.json()
        return response

    def _request_post(self, path, data=None, params=None, url=BASE_URL):
        url = urljoin(url, path)
        headers = self._get_request_headers()
        response = requests.post(url, json=data, params=params, headers=headers)
        response.raise_for_status()
        return response

    def _request_put(self, path, data=None, params=None, url=BASE_URL):
        url = urljoin(url, path)
        headers = self._get_request_headers()
        response = requests.put(url, json=data, params=params, headers=headers)
        response.raise_for_status()
        if response.status_code == status.HTTP_200_OK:
            return response.json()

    def _request_delete(self, path, params=None, url=BASE_URL):
        url = urljoin(url, path)
        headers = self._get_request_headers()
        response = requests.delete(url, params=params, headers=headers)
        response.raise_for_status()
        if response.status_code == status.HTTP_200_OK:
            return response.json()
