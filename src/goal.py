class Goal:
    def __init__(self, retirement_age: int, passive_income_goal: float, monthly_contributions: float,
                 annual_contribution_increase: float, max_contribution_expectation: float, investor_profile: str):
        self._retirement_age = retirement_age
        self._passive_income_goal = passive_income_goal
        self._monthly_contributions = monthly_contributions
        self._annual_contribution_increase = annual_contribution_increase
        self._max_contribution_expectation = max_contribution_expectation
        self._investor_profile = investor_profile
        self.total_accumulated = 0
        self.total_interest = 0
        self.total_invested = 0
        self.passive_income_generated = 0

    @property
    def retirement_age(self):
        return self._retirement_age

    @retirement_age.setter
    def retirement_age(self, value: int):
        self._retirement_age = value

    @property
    def passive_income_goal(self):
        return self._passive_income_goal

    @passive_income_goal.setter
    def passive_income_goal(self, value: float):
        self._passive_income_goal = value

    @property
    def monthly_contributions(self):
        return self._monthly_contributions

    @monthly_contributions.setter
    def monthly_contributions(self, value: float):
        self._monthly_contributions = value

    @property
    def annual_contribution_increase(self):
        return self._annual_contribution_increase

    @annual_contribution_increase.setter
    def annual_contribution_increase(self, value: float):
        self._annual_contribution_increase = value

    @property
    def max_contribution_expectation(self):
        return self._max_contribution_expectation

    @max_contribution_expectation.setter
    def max_contribution_expectation(self, value: float):
        self._max_contribution_expectation = value

    @property
    def investor_profile(self):
        return self._investor_profile

    @investor_profile.setter
    def investor_profile(self, value: str):
        self._investor_profile = value

    def calculate_investment_period(self, current_age: int):
        years_to_retirement = self._retirement_age - current_age
        if years_to_retirement <= 0:
            return

        # Cálculo básico de contribuições e juros
        total_invested = self._monthly_contributions * 12 * years_to_retirement
        interest_rate = 0.05  # Taxa de juros anual (5%)
        total_interest = total_invested * interest_rate * years_to_retirement
        total_accumulated = total_invested + total_interest
        passive_income_generated = total_accumulated * 0.04  # Suposição de 4% de renda passiva gerada anualmente

        # Armazenar valores calculados nos atributos da classe
        self.total_accumulated = total_accumulated
        self.total_interest = total_interest
        self.total_invested = total_invested
        self.passive_income_generated = passive_income_generated

        return {
            "total_accumulated": total_accumulated,
            "total_interest": total_interest,
            "total_invested": total_invested,
            "passive_income_generated": passive_income_generated
        }
