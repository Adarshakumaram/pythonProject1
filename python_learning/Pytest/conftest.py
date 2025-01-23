import pytest
import  requests
import os
from  dotenv import load_dotenv

@pytest.fixture()
def create_token():
    load_dotenv()
    username=os.getenv("USERNAME1")
    password=os.getenv("PASSWORD")
    print()
    #print(username,password)
    print("Creating token ...")
    head = {"Content-Type": "application/json"}
    url = "https://restful-booker.herokuapp.com/auth"
    json_payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url=url, headers=head, json=json_payload)
    data = response.json()["token"]
    #print(data)
    return data




@pytest.fixture()
def create_booking_id():
    print("Creating booking id  ....")
    url_1 = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Amt",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=url_1, headers=headers, json=payload)
    data = response_data.json()
    booking_id = data["bookingid"]
    #print(booking_id)
    return booking_id
