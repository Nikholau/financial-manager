from income import Income
from expense import Expense
from investor_profile import InvestorProfile
from objective import Objective
import json
from typing import List

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

    def save_to_file(self, file_name: str) -> None:
        data = {
            "name": self.name,
            "age": self.age,
            "income": [{"type": inc.type, "amount": inc.amount, "date": inc.date.strftime('%Y-%m-%d')} for inc in self._income],
            "expenses": [{"type": exp.type, "amount": exp.amount, "date": exp.date.strftime('%Y-%m-%d')} for exp in self._expenses],
            "profile": {
                "profile_type": self._profile.profile_type,
                "description": self._profile.description
            } if self._profile else None,
            "objectives": [{
                "objective_type": obj.objective_type,
                "description": obj.description,
                "goals": [{
                    "retirement_age": goal.retirement_age,
                    "passive_income_goal": goal.passive_income_goal,
                    "total_accumulated": goal.total_accumulated,
                    "total_interest": goal.total_interest,
                    "total_invested": goal.total_invested
                } for goal in obj._goals]
            } for obj in self._objectives]
        }

        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, file_name: str) -> 'User':
        with open(file_name, 'r') as f:
            data = json.load(f)
        
        # Reconstruir o objeto User a partir dos dados carregados
        user = cls(name=data["name"], age=data["age"])
        user._income = [Income(type=inc["type"], amount=inc["amount"], date=datetime.strptime(inc["date"], '%Y-%m-%d')) for inc in data["income"]]
        user._expenses = [Expense(type=exp["type"], amount=exp["amount"], date=datetime.strptime(exp["date"], '%Y-%m-%d')) for exp in data["expenses"]]
        
        if data["profile"]:
            user._profile = Profile(profile_type=data["profile"]["profile_type"], description=data["profile"]["description"])
        
        user._objectives = []
        for obj in data["objectives"]:
            objective = Objective(objective_type=obj["objective_type"], description=obj["description"])
            objective._goals = [
                Goal(
                    retirement_age=goal["retirement_age"],
                    passive_income_goal=goal["passive_income_goal"],
                    total_accumulated=goal.get("total_accumulated", 0.0),
                    total_interest=goal.get("total_interest", 0.0),
                    total_invested=goal.get("total_invested", 0.0)
                ) for goal in obj["goals"]
            ]
            user._objectives.append(objective)

        return user
