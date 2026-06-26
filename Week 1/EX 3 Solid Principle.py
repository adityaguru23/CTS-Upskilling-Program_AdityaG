from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class PaymentService:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.pay(amount)

service = PaymentService(CreditCard())
service.make_payment(500)

service = PaymentService(UPI())
service.make_payment(250)