from http.client import responses

import pytest
import allure
import requests

@allure.title('Get request test')
@allure.description('should work with requests')
@pytest.mark.positive
def test_request_positive():
    URL="https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url = URL)
    print(response_data.text)
    assert response_data.status_code ==200

def test_request_negative():
    URL="https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url = URL)
    print(response_data.text)
    assert response_data.status_code ==404
