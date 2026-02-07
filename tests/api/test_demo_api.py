from api.api_client import APIClient

def test_demo_api():
    api = APIClient()
    response = api.get("https://httpbin.org/get")
    assert response.status_code == 200

def test_put_demo():
    api = APIClient()
    payload = {"name": "framework"}
    response = api.put("https://httpbin.org/put", payload)

    assert response.status_code == 200
