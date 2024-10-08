from datetime import datetime
from income import Income
from expense import Expense
from investor_profile import InvestorProfile
from goal import Goal
from objective import Objective
from user import User
from report import Report
import os

def main():
    try:
        file_name = "user_data.json"
        if os.path.exists(file_name):
            carregar = input("Deseja carregar os dados do usuário existente? (s/n): ").lower()
            if carregar == 's':
                usuario = User.load_from_file(file_name)
                print(f"Bem-vindo de volta, {usuario.name}!")
            else:
                usuario = criar_novo_usuario(file_name)
        else:
            usuario = criar_novo_usuario(file_name)

        adicionar_rendas_despesas(usuario)

        tipo_perfil = input("Digite o seu perfil de investidor (Conservador, Moderado, Agressivo): ")
        perfil = InvestorProfile(profile_type=tipo_perfil)
        usuario.set_profile(perfil)

        tipo_objetivo = input("Digite o seu objetivo financeiro: ")
        descricao_objetivo = input("Digite uma descrição para o seu objetivo: ")
        objetivo = Objective(objective_type=tipo_objetivo, description=descricao_objetivo)
        usuario.add_objective(objetivo)

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
            max_contribution_expectation=expectativa_maxima_contribuicao,
            investor_profile=tipo_perfil
        )

        resultado_meta = meta.calculate_investment_period(current_age=usuario.age)


        objetivo.add_goal(meta)

        relatorio = Report(user=usuario)
        relatorio.add_goal_data(
            total_accumulated=meta.total_accumulated,
            total_interest=meta.total_interest,
            total_invested=meta.total_invested,
            passive_income_generated=meta.passive_income_generated
        )

        relatorio.generate_pdf("relatorio_usuario.pdf")

        usuario.save_to_file(file_name)

        print("Relatório gerado com sucesso! O arquivo PDF foi salvo como 'relatorio_usuario.pdf'.")
        print(f"Dados do usuário foram salvos em '{file_name}'.")

    except ValueError as e:
        print(f"Erro de valor inválido: {e}. Por favor, insira os dados corretamente.")
    except FileNotFoundError as e:
        print(f"Erro: arquivo não encontrado - {e}")
    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def criar_novo_usuario(file_name: str) -> User:
    try:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        usuario = User(name=nome, age=idade)
        usuario.save_to_file(file_name)
        return usuario
    except ValueError as e:
        print(f"Erro de valor inválido ao criar usuário: {e}")

def adicionar_rendas_despesas(usuario: User) -> None:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        usuario.add_income(Income(type="Salário", amount=salario, date=datetime.now()))

        aluguel = float(input("Digite o valor do seu gasto com aluguel: "))
        usuario.add_expense(Expense(type="Aluguel", amount=aluguel, date=datetime.now()))
    except ValueError as e:
        print(f"Erro de valor inválido ao adicionar renda ou despesa: {e}")

if __name__ == "__main__":
    main()
