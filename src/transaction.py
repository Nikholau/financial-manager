from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    def __init__(self, type: str, amount: float, date: datetime):
        self._type = type
        self._amount = amount
        self._date = date

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value: float):
        self._amount = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value: datetime):
        self._date = value

    @abstractmethod
    def calculate_total_annual(self) -> float:
        pass
