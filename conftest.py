import pytest
import requests
from helpers.booking import Booking

fixture = None

BASE_URL = "https://restful-booker.herokuapp.com/booking/"
USERNAME = "admin"
PASSWORD = "password123"


@pytest.fixture(scope="session")
def get_token(request):
    response = requests.post(f"{BASE_URL}/auth", json={"username": USERNAME, "password": PASSWORD})
    response.raise_for_status()
    return response.json()['token']


@pytest.fixture(scope="session")
def booking(request):
    fixture = Booking(BASE_URL)
    return fixture
