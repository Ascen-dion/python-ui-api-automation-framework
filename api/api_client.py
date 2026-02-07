import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class APIClient:

    def get(self, url, params=None):
        return requests.get(url, params=params, verify=False)

    def post(self, url, payload=None):
        return requests.post(url, json=payload, verify=False)
