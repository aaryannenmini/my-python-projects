from abc import ABC,abstractmethod


class vehicle(ABC):
     @abstractmethod
     def num_wheel(self):
          pass
class bike(vehicle):
     def num_wheel(self):
          return 2
class car(vehicle):
     def num_wheel(self):
          return 4
     
Motorcycle = bike()
Four_Wheeler = car()

print(f"A bike has {Motorcycle.num_wheel()} wheels and a car has {Four_Wheeler.num_wheel()} wheels")

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Process the payment of the specified amount."""
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")

# Creating instances of payment methods
credit_card = CreditCardPayment()
paypal = PayPalPayment()

# Directly calling the methods to make payments
credit_card.process_payment(50.00)
paypal.process_payment(30.75)