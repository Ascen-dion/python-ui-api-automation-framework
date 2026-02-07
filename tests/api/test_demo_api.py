from api.api_client import APIClient


def test_demo_api():
    api = APIClient()
    response = api.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200


def test_put_demo():
    api = APIClient()

    payload = {"title": "updated"}
    response = api.put("https://jsonplaceholder.typicode.com/posts/1", payload)

    assert response.status_code in [200, 201]
