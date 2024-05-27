import logging

from model.booking_data import CreateBooking
from helpers.booking_query import BookingQuery
from model.booking_model import BookingModel
from pydantic import ValidationError
import random
from datetime import date, timedelta


class Booking:
    def __init__(self, base_url):
        self.booking = BookingQuery
        self.url = base_url

    def create_booking(self):
        new_booking = BookingQuery().create_booking(self.url, CreateBooking(), code=200)
        return new_booking

    def get_any_bookingid(self):
        booking_list = BookingQuery().get_bookings_list(url=self.url)
        return random.choice(booking_list)["bookingid"]

    def get_booking_by_id(self, id):
        return BookingQuery().get_bookings_by_id(url=self.url, id=id)

    def update_booking(self, existing_booking, id, new_data):
        return BookingQuery().update_booking(url=self.url, existing_booking=existing_booking, id=id,
                                             price=new_data['price'],
                                             checkin=new_data['checkin'], checkout=new_data['checkout'])

    def partial_update_booking(self, id, new_data):
        return BookingQuery().partial_update_booking(url=self.url, id=id, price=new_data['price'],
                                                     checkin=new_data['checkin'], checkout=new_data['checkout'])

    def create_new_booking_data(self):
        price = random.randrange(1000, 10000)
        checkin = date.today() + timedelta(days=5)
        checkout = checkin + timedelta(days=7)
        new_data = {'price': price, 'checkin': str(checkin), 'checkout': str(checkout)}
        return new_data

    def delete_booking(self, id):
        BookingQuery().delete_booking(self.url, id)

    # Verification functions
    def verify_booking_id_not_null(self, booking):
        assert booking["bookingid"] is not None

    def verify_booking_data(self, booking):
        assert booking["booking"]["firstname"] == CreateBooking().firstname
        assert booking["booking"]["lastname"] == CreateBooking().lastname
        assert booking["booking"]["totalprice"] == CreateBooking().totalprice
        assert booking["booking"]["depositpaid"] == CreateBooking().depositpaid
        assert booking["booking"]["bookingdates"]["checkin"] == CreateBooking().checkin
        assert booking["booking"]["bookingdates"]["checkout"] == CreateBooking().checkout
        assert booking["booking"]["additionalneeds"] == CreateBooking().additionalneeds

    def validate_schema(self, body):
        try:
            BookingModel.model_validate_json(body)
            return True
        except ValidationError as e:
            logging.error(e.json())
            return False

    def verify_response_schema(self, body):
        assert self.validate_schema(body) is True, "Response isn't valid"

    def verify_booking_is_update(self, response, expected_data):
        assert response["totalprice"] == expected_data['price']
        assert response["bookingdates"]["checkin"] == expected_data['checkin']
        assert response["bookingdates"]["checkout"] == expected_data['checkout']

    def verify_partial_update_booking_success(self, response, expected_data):
        assert response["totalprice"] == expected_data['price']
        assert response["bookingdates"]["checkin"] == expected_data['checkin']
        assert response["bookingdates"]["checkout"] == expected_data['checkout']
        assert response["firstname"] is not None
        assert response["lastname"] is not None

    def verify_booking_is_delete(self, id):
        test = BookingQuery().get_bookings_by_id(self.url, id)
        assert test == 404, "Booking wasn't delete"

