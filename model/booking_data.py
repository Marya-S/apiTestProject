class CreateBooking:
    def __init__(self, firstname="Jim", lastname="Carrey", totalprice=12500, depositpaid=True,
                 checkin="2024-07-01", checkout="2024-07-10", additionalneeds="Breakfast"):
        self.firstname = firstname
        self.lastname = lastname
        self.totalprice = totalprice
        self.depositpaid = depositpaid
        self.checkin = checkin
        self.checkout = checkout
        self.additionalneeds = additionalneeds
