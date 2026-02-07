import requests
import urllib3
import allure
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class APIClient:

    def get(self, url, params=None):
        with allure.step(f"GET Request → {url}"):
            self._attach_payload("Query Params", params)

            response = requests.get(url, params=params, verify=False)
            self._attach_response(response)
            return response

    def post(self, url, payload=None):
        with allure.step(f"POST Request → {url}"):
            self._attach_payload("Request Body", payload)

            response = requests.post(url, json=payload, verify=False)
            self._attach_response(response)
            return response

    def put(self, url, payload=None):
        with allure.step(f"PUT Request → {url}"):
            self._attach_payload("Request Body", payload)

            response = requests.put(url, json=payload, verify=False)
            self._attach_response(response)
            return response

    def patch(self, url, payload=None):
        with allure.step(f"PATCH Request → {url}"):
            self._attach_payload("Request Body", payload)

            response = requests.patch(url, json=payload, verify=False)
            self._attach_response(response)
            return response

    def delete(self, url):
        with allure.step(f"DELETE Request → {url}"):

            response = requests.delete(url, verify=False)
            self._attach_response(response)
            return response

    # -------------------------
    # Helpers
    # -------------------------

    def _attach_payload(self, name, payload):
        if payload:
            allure.attach(
                json.dumps(payload, indent=2),
                name,
                allure.attachment_type.JSON
            )

    def _attach_response(self, response):
        allure.attach(
            str(response.status_code),
            "Status Code",
            allure.attachment_type.TEXT
        )

        try:
            allure.attach(
                json.dumps(response.json(), indent=2),
                "Response Body",
                allure.attachment_type.JSON
            )
        except Exception:
            allure.attach(
                response.text,
                "Response Body",
                allure.attachment_type.TEXT
            )

        allure.attach(
            json.dumps(dict(response.headers), indent=2),
            "Response Headers",
            allure.attachment_type.JSON
        )
