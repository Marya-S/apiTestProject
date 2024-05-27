## test for service https://restful-booker.herokuapp.com/apidoc/index.html
import json


def test_create_new_booking(booking):
    new_booking = booking.create_booking()
    booking.verify_booking_id_not_null(new_booking)
    booking.verify_booking_data(new_booking)


def test_get_existing_booking(booking):
    existing_booking_id = booking.get_any_bookingid()
    response = booking.get_booking_by_id(existing_booking_id, 200)
    booking.verify_response_schema(json.dumps(response))


def test_update_booking(booking):
    existing_booking_id = booking.get_any_bookingid()
    existing_booking = booking.get_booking_by_id(existing_booking_id)
    new_data = booking.create_new_booking_data()
    response = booking.update_booking(existing_booking, existing_booking_id, new_data)
    booking.verify_booking_is_update(response, new_data)


def test_partial_booking_update(booking):
    existing_booking_id = booking.get_any_bookingid()
    new_data = booking.create_new_booking_data()
    response = booking.partial_update_booking(existing_booking_id, new_data)
    booking.verify_partial_update_booking_success(response, new_data)


def test_delete_booking(booking):
    existing_booking_id = booking.get_any_bookingid()
    booking.delete_booking(existing_booking_id)
    booking.verify_booking_is_delete(existing_booking_id)
