class Goal:
    def __init__(self, retirement_age, passive_income_goal, monthly_contributions, 
                 annual_contribution_increase, max_contribution_expectation, investor_profile):
        self.retirement_age = retirement_age
        self.passive_income_goal = passive_income_goal
        self.monthly_contributions = monthly_contributions
        self.annual_contribution_increase = annual_contribution_increase
        self.max_contribution_expectation = max_contribution_expectation
        self.investor_profile = investor_profile

        # Inicializando variáveis que serão calculadas
        self.total_accumulated = 0.0
        self.total_interest = 0.0
        self.total_invested = 0.0
        self.passive_income_generated = 0.0

    def calculate_investment_period(self, current_age):
        # Calculando o período de investimento
        years_to_invest = self.retirement_age - current_age
        
        if years_to_invest <= 0:
            raise ValueError("A idade de aposentadoria deve ser maior que a idade atual.")

        # Variáveis para acumular valores ao longo dos anos
        accumulated = 0.0
        total_invested = 0.0
        annual_contribution = self.monthly_contributions * 12

        for year in range(years_to_invest):
            # Adiciona a contribuição anual
            total_invested += annual_contribution
            # Supondo um retorno anual médio (ex: 5%)
            interest_rate = 0.05
            accumulated = (accumulated + annual_contribution) * (1 + interest_rate)

            # Aumentando a contribuição anual, até o máximo permitido
            annual_contribution = min(annual_contribution * (1 + self.annual_contribution_increase / 100), 
                                      self.max_contribution_expectation * 12)

        # Calculando a renda passiva com base no valor acumulado
        passive_income_generated = accumulated * 0.04  # Supondo que você retire 4% ao ano

        # Atribuir os valores calculados
        self.total_accumulated = accumulated
        self.total_interest = accumulated - total_invested
        self.total_invested = total_invested
        self.passive_income_generated = passive_income_generated

        return {
            "total_accumulated": self.total_accumulated,
            "total_interest": self.total_interest,
            "total_invested": self.total_invested,
            "passive_income_generated": self.passive_income_generated
        }
