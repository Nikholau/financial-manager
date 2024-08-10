from datetime import datetime
from income import Income
from expense import Expense
from investor_profile import InvestorProfile
from goal import Goal
from objective import Objective
from user import User
from report import Report

def main():
    # Coletar dados do usuário
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Criar instância de User
    user = User(name=name, age=age)

    # Coletar rendas
    salary = float(input("Enter your salary: "))
    user.add_income(Income(type="Salary", amount=salary, date=datetime.now()))

    # Coletar despesas
    rent = float(input("Enter your rent expense: "))
    user.add_expense(Expense(type="Rent", amount=rent, date=datetime.now()))

    # Definir perfil do investidor
    profile_type = input("Enter your investor profile (Conservative, Moderate, Aggressive): ")
    profile_description = input("Enter a description for your investor profile: ")
    profile = InvestorProfile(profile_type=profile_type, description=profile_description)
    user.set_profile(profile)

    # Definir objetivos
    objective_type = input("Enter your financial objective: ")
    objective_description = input("Enter a description for your objective: ")
    objective = Objective(objective_type=objective_type, description=objective_description)
    user.add_objective(objective)

    # Exemplo de adição de meta ao objetivo
    retirement_age = int(input("Enter your target retirement age: "))
    passive_income_goal = float(input("Enter your passive income goal: "))
    monthly_contributions = float(input("Enter your monthly contribution: "))
    annual_contribution_increase = float(input("Enter your annual contribution increase (in %): "))
    max_contribution_expectation = float(input("Enter your maximum contribution expectation: "))

    goal = Goal(
        retirement_age=retirement_age,
        passive_income_goal=passive_income_goal,
        monthly_contributions=monthly_contributions,
        annual_contribution_increase=annual_contribution_increase,
        max_contribution_expectation=max_contribution_expectation
    )
    objective.add_goal(goal)

    # Gerar relatório
    report = user.generate_report()
    print(report.generate())

if __name__ == "__main__":
    main()
