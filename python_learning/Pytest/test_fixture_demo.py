import  pytest

@pytest.fixture()
def create_token():
    return "sdf"

@pytest.fixture()
def create_boooking():
    return 1

@pytest.fixture()
def read_excel():
    return "asdf"

def test_put(create_token,create_boooking,read_excel):
    print()
    print(create_boooking)
    print(create_token)
    print(read_excel)