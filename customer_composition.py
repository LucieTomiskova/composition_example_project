from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Payment(ABC):
    """Represents payment methods"""

    @abstractmethod
    def convert_payment(self):
        """Process payment according the type"""


class Currency(ABC):
    """Represents currency and its exchange rate"""

    @abstractmethod
    def get_exchange_rate(self):
        """Retrieve current exchange rate"""


class USD(Currency):

    exchange_rate: float = 21.5

    def get_exchange_rate(self):
        print("Fetching current exchange rate...")
        print(f"Exchange rate is: {self.exchange_rate}")
        return self.exchange_rate


class EUR(Currency):

    exchange_rate: float = 25.3

    def get_exchange_rate(self):
        print("Fetching current exchange rate...")
        print(f"Exchange rate is: {self.exchange_rate}")
        return self.exchange_rate


@dataclass
class CardPayment(Payment):
    """Class for calculating card payment.
    Card payment can be done in several currencies."""

    provider: str
    amount: float
    currency: Optional[Currency] = None

    def convert_payment(self):
        if self.currency:
            exchange_rate = self.currency.get_exchange_rate()
            return self.amount * exchange_rate
        return self.amount



@dataclass
class CashPayment(Payment):
    """Class for calculating cash payment.
    Cash payment can be done only in home currency."""

    amount: float


@dataclass
class PaymentProcessor:

    id: int
    payment: Payment
    tax: float = 0.15
    home_currency: str = 'CZK'

    def get_paid_amount(self):
        return self.payment.convert_payment()

    def process_payment(self, amount: float):
        print(f"Payment: {amount} {self.home_currency} is being processed.")

    def calculate_payment_after_tax(self, amount: float):
        amount_after_tax = amount - (amount * self.tax)
        print(f"Amount after tax is: {amount_after_tax} {self.home_currency}")
        return amount_after_tax


if __name__ == '__main__':
    payment_by_lucie = CardPayment(provider='VISA', amount=9.5, currency=USD())

    payment_process = PaymentProcessor(id=1, payment=payment_by_lucie)
    paid_amount = payment_process.get_paid_amount()
    payment_process.process_payment(paid_amount)
    payment_process.calculate_payment_after_tax(paid_amount)
