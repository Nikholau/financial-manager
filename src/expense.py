from datetime import datetime
from transaction import Transaction

class Expense(Transaction):
    def __init__(self, type: str, amount: float, date: datetime):
        super().__init__(type, amount, date)

    def calculate_total_annual(self) -> float:
        return -self.amount * 12
