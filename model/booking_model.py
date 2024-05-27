from typing import List, Dict

from pydantic import BaseModel


class Dates(BaseModel):
    checkin: str
    checkout: str


class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: Dates
    additionalneeds: str


