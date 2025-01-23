from ctypes import pydll
from http.client import responses
from tokenize import String

import allure
import pytest
import requests
from requests import Response


@allure.title("TC#1 create booking crud positive")
@allure.description("TC#1 verify the create booking ")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url="https://restful-booker.herokuapp.com"
    path_url="/booking"
    full_url = base_url+path_url
    headers ={
        "Content-Type" : "application/json"
    }
    payload ={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

    response_data = requests.post(url=full_url,headers=headers, json=payload)
    #status code verification
    assert response_data.status_code == 200

    #booking
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    print(bookingid)
    assert bookingid is not None
    assert bookingid >=1
    assert type(bookingid) == int

    firstname = response_data_json["booking"]["firstname"]
    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    depositpaid = response_data_json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert totalprice ==111
    assert depositpaid == True

    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout = response_data_json["booking"]["bookingdates"]["checkout"]
    assert  checkin == "2018-01-01"
    assert  checkout == "2019-01-01"

    time= response_data.elapsed.total_seconds()
    assert time < 3




@allure.title("TC#1 create booking crud negative")
@allure.description("TC#1 verify the invalid payload booking")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking"
    URL = base_url + path_url
    head = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL,headers=head,json=json_payload)
    print(response.text)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"