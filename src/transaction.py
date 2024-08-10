from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

# Abstract Base Class for Transactions
class Transaction(ABC):
    def __init__(self, type: str, amount: float, date: datetime):
        self._type = type
        self._amount = amount
        self._date = date

    @property
    def type(self):
        return self._type

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._date

    @abstractmethod
    def calculate_total_annual(self) -> float:
        pass