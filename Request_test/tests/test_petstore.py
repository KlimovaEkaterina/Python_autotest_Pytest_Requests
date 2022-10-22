import pytest
import requests

url="https://petstore.swagger.io/v2/pet/1555"

# В ответе поиска питомца с id=1555 приходит статус код 200
def test_status_code():
    response=requests.get(url)
    assert response.status_code == 200

# В ответе поиска питомца с id=1555 приходит имя питомца Lucky
def test_check_response():
    response=requests.get(url)
    response=response.json()
    assert response["name"] == "Lucky"