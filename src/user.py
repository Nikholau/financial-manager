from income import Income
from expense import Expense
from investor_profile import InvestorProfile
from objective import Objective

class User:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self._profile = None
        self._objectives = []
        self._income = []
        self._expenses = []

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def add_income(self, income: Income) -> None:
        self._income.append(income)

    def add_expense(self, expense: Expense) -> None:
        self._expenses.append(expense)

    def set_profile(self, profile: InvestorProfile) -> None:
        self._profile = profile

    def add_objective(self, objective: Objective) -> None:
        self._objectives.append(objective)

    def generate_report(self) -> 'Report':
        # Implementation for generating a report
        pass
