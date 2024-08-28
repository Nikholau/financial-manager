class Goal:
    def __init__(self, retirement_age: int, passive_income_goal: float, monthly_contributions: float,
                 annual_contribution_increase: float, max_contribution_expectation: float, investor_profile: str):
        self.retirement_age = retirement_age
        self.passive_income_goal = passive_income_goal
        self.monthly_contributions = monthly_contributions
        self.annual_contribution_increase = annual_contribution_increase
        self.max_contribution_expectation = max_contribution_expectation
        self.investor_profile = investor_profile

        # Atributos para armazenar os resultados do cálculo
        self.total_accumulated = 0.0
        self.total_interest = 0.0
        self.total_invested = 0.0

    def calculate_investment_period(self, current_age: int):
        # Implementação do cálculo...
        # Após o cálculo, você pode armazenar os resultados nos atributos:
        self.total_accumulated = 100000.0  # Exemplo de valor calculado
        self.total_interest = 20000.0  # Exemplo de valor calculado
        self.total_invested = 80000.0  # Exemplo de valor calculado

        return {
            "total_accumulated": self.total_accumulated,
            "total_interest": self.total_interest,
            "total_invested": self.total_invested,
            "passive_income_generated": 1500.0  # Exemplo de valor calculado
        }
