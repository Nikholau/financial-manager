from datetime import datetime
from income import Income
from expense import Expense
from investor_profile import InvestorProfile
from goal import Goal
from objective import Objective
from user import User
from report import Report

def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    usuario = User(name=nome, age=idade)

    salario = float(input("Digite o valor do seu salário: "))
    usuario.add_income(Income(type="Salário", amount=salario, date=datetime.now()))

    aluguel = float(input("Digite o valor do seu gasto com aluguel: "))
    usuario.add_expense(Expense(type="Aluguel", amount=aluguel, date=datetime.now()))

    # Definir perfil do investidor
    tipo_perfil = input("Digite o seu perfil de investidor (Conservador, Moderado, Agressivo): ")
    descricao_perfil = input("Digite uma descrição para o seu perfil de investidor: ")
    perfil = InvestorProfile(profile_type=tipo_perfil, description=descricao_perfil)
    usuario.set_profile(perfil)

    # Definir objetivos
    tipo_objetivo = input("Digite o seu objetivo financeiro: ")
    descricao_objetivo = input("Digite uma descrição para o seu objetivo: ")
    objetivo = Objective(objective_type=tipo_objetivo, description=descricao_objetivo)
    usuario.add_objective(objetivo)

    # Adição de meta ao objetivo
    idade_aposentadoria = int(input("Digite a idade em que deseja se aposentar: "))
    meta_renda_passiva = float(input("Digite o valor da sua meta de renda passiva: "))
    contribuicoes_mensais = float(input("Digite o valor das suas contribuições mensais: "))
    aumento_anual_contribuicao = float(input("Digite o percentual de aumento anual das contribuições (em %): "))
    expectativa_maxima_contribuicao = float(input("Digite o valor máximo da sua expectativa de contribuição: "))

    meta = Goal(
        retirement_age=idade_aposentadoria,
        passive_income_goal=meta_renda_passiva,
        monthly_contributions=contribuicoes_mensais,
        annual_contribution_increase=aumento_anual_contribuicao,
        max_contribution_expectation=expectativa_maxima_contribuicao
    )
    objetivo.add_goal(meta)

    # Gerar relatório em PDF
    relatorio = Report(user=usuario)
    relatorio.generate_pdf("relatorio_usuario.pdf")

    print("Relatório gerado com sucesso! O arquivo PDF foi salvo como 'relatorio_usuario.pdf'.")

if __name__ == "__main__":
    main()
