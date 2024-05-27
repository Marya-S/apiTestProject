import requests
import json
import pytest
import logging
from urllib3.exceptions import InsecureRequestWarning


class BookingQuery:
    def create_booking(self, url, booking, code):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            "firstname": booking.firstname,
            "lastname": booking.lastname,
            "totalprice": booking.totalprice,
            "depositpaid": booking.depositpaid,
            "bookingdates": {
                "checkin": booking.checkin,
                "checkout": booking.checkout
            },
            "additionalneeds": booking.additionalneeds
        }
        url = url
        logging.info("url: %s" % url)
        logging.info("headers: %s" % headers)
        logging.info("body: %s" % body)
        response = requests.post(url, headers=headers, data=json.dumps(body), verify=False)
        if response.status_code == code:
            logging.info("response: %s" % response.json())
            return response.json()
        else:
            try:
                pytest.fail("booking not created"
                            "\n status code: " + str(response.status_code) +
                            "\n body: " + str(response.json()))
            except json.decoder.JSONDecodeError:
                pytest.fail("booking not created"
                            "\n status code: " + str(response.status_code))

    def get_bookings_list(self, url):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        headers = {
            'Content-Type': 'application/json'
        }
        url = url
        logging.info("url: %s" % url)
        logging.info("headers: %s" % headers)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            logging.info("response: %s" % response.json())
            return response.json()
        else:
            try:
                pytest.fail("booking isn't return"
                            "\n status code: " + str(response.status_code) +
                            "\n body: " + str(response.json()))
            except json.decoder.JSONDecodeError:
                pytest.fail("booking isn't return"
                            "\n status code: " + str(response.status_code))

    def get_bookings_by_id(self, url, id):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        headers = {
            'Content-Type': 'application/json'
        }
        url = url + str(id)
        logging.info("url: %s" % url)
        logging.info("headers: %s" % headers)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            logging.info("response: %s" % response.json())
            return response.json()
        else:
            try:
                logging.error("booking isn't return. Error " + str(response.status_code) + " " + response.reason)
                return response.status_code
            except json.decoder.JSONDecodeError:
                pytest.fail("booking isn't return"
                            "\n status code: " + str(response.status_code) + " " + response.reason)
                return response.status_code

    def update_booking(self, url, existing_booking, id, price, checkin, checkout):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }
        body = {
            "firstname": existing_booking['firstname'],
            "lastname": existing_booking['lastname'],
            "totalprice": price,
            "depositpaid": existing_booking['depositpaid'],
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": "late breakfast"
        }
        url = url + str(id)
        logging.info("url: %s" % url)
        logging.info("headers: %s" % headers)
        logging.info("body: %s" % body)
        response = requests.put(url, headers=headers, data=json.dumps(body), verify=False)
        if response.status_code == 200:
            logging.info("response: %s" % response.json())
            return response.json()
        else:
            try:
                pytest.fail("booking not update"
                            "\n status code: " + str(response.status_code) +
                            "\n body: " + str(response.json()))
            except json.decoder.JSONDecodeError:
                pytest.fail("booking not update"
                            "\n status code: " + str(response.status_code))

    def partial_update_booking(self, url, id, price, checkin, checkout):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }
        body = {
            "totalprice": price,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
        }
        url = url + str(id)
        logging.info("url: %s" % url)
        logging.info("headers: %s" % headers)
        logging.info("body: %s" % body)
        response = requests.patch(url, headers=headers, data=json.dumps(body), verify=False)
        if response.status_code == 200:
            logging.info("response: %s" % response.json())
            return response.json()
        else:
            try:
                pytest.fail("booking not update"
                            "\n status code: " + str(response.status_code) +
                            "\n body: " + str(response.json()))
            except json.decoder.JSONDecodeError:
                pytest.fail("booking not update"
                            "\n status code: " + str(response.status_code))

    def delete_booking(self, url, id):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }
        url = url + str(id)
        logging.info("url: %s" % url)
        logging.info("headers: %s" % headers)
        response = requests.delete(url, headers=headers)
        if response.status_code == 201:
            logging.info("response: %s" % str(response.status_code) + " " + response.reason)
        else:
            try:
                pytest.fail("booking isn't delete"
                            "\n status code: " + str(response.status_code) + " " + response.reason)
            except json.decoder.JSONDecodeError:
                pytest.fail("booking isn't delete"
                            "\n status code: " + str(response.status_code))
