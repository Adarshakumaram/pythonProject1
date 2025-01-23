from http.client import responses
from wsgiref.validate import header_re

import requests

head = {"Content-Type": "application/json"}
base_url = "https://restful-booker.herokuapp.com"
def get_token():
    path_url="/auth"
    json_payload={
    "username" : "admin",
    "password" : "password123"
    }
    full_url = base_url+path_url
    response = requests.post(url=full_url,headers=head,json=json_payload)

    assert response.status_code ==200
    response_json = response.json()
    token =response_json["token"]
    print(token)
    assert type(token) ==str
    assert len(token) >0
    return token

def get_booking_id():
    path_url = "/booking"
    full_url = base_url + path_url
    headers = { "Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
        }
    response_data = requests.post(url=full_url, headers=headers, json=payload)
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    return bookingid

def test_put_request():
    token = get_token()
    bookingid =get_booking_id()
    print(token)
    print(bookingid)
    base_path = "/booking/" + str(bookingid)
    full_put_url = base_url +base_path
    print(full_put_url)
    cookie = "token="+token
    print(cookie)
    headers = { "Content-Type": "application/json",
    "Cookie":cookie}
    payload = {
        "firstname": "Adhu",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=full_put_url,headers=headers,json=payload)
    print(response)
    assert  response.status_code ==200
    assert response.json()["firstname"] == "Adhu"

def test_delete():
    url = "https://restful-booker.herokuapp.com/booking/"
    booking_id = get_booking_id()
    delete_url = url +str(booking_id)
    cookie_value = "token=" + get_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    response = requests.delete(url=delete_url,headers=headers)
    assert response.status_code ==201

