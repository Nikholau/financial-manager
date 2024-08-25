class Goal:
    def __init__(self, retirement_age: int, passive_income_goal: float, 
                 monthly_contributions: float, annual_contribution_increase: float, 
                 max_contribution_expectation: float, investor_profile: str):
        self.retirement_age = retirement_age
        self.passive_income_goal = passive_income_goal
        self.monthly_contributions = monthly_contributions
        self.annual_contribution_increase = annual_contribution_increase
        self.max_contribution_expectation = max_contribution_expectation
        self.investor_profile = investor_profile
        self.annual_return_rate = self._get_annual_return_rate()

    def _get_annual_return_rate(self) -> float:
        if self.investor_profile == "Conservador":
            return 0.06
        elif self.investor_profile == "Moderado":
            return 0.10
        elif self.investor_profile == "Agressivo":
            return 0.14
        else:
            raise ValueError("Perfil de investidor inválido.")

    def calculate_investment_period(self, current_age: int) -> dict:
        total_years = self.retirement_age - current_age
        current_contribution = self.monthly_contributions
        total_invested = 0
        total_accumulated = 0

        for year in range(total_years):
            yearly_contribution = 0

            for month in range(12):
                yearly_contribution += current_contribution

            total_invested += yearly_contribution
            total_accumulated = (total_accumulated + yearly_contribution) * (1 + self.annual_return_rate)

            # Incremento anual das contribuições, limitado pela contribuição máxima esperada
            current_contribution = min(current_contribution * (1 + self.annual_contribution_increase / 100),
                                       self.max_contribution_expectation)

        total_interest = total_accumulated - total_invested

        # Cálculo da renda passiva mensal com base na taxa de retorno anual
        passive_income_generated = (total_accumulated * self.annual_return_rate) / 12

        return {
            "total_accumulated": total_accumulated,
            "total_interest": total_interest,
            "total_invested": total_invested,
            "passive_income_generated": passive_income_generated
        }
