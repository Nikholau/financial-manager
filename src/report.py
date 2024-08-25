from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from flask import Flask, send_file
from user import User

app = Flask(__name__)

class Report:
    def __init__(self, user: User):
        self._user = user
        self._generation_date = datetime.now()
        self._goal_data = {}

    def add_goal_data(self, total_accumulated: float, total_interest: float, 
                      total_invested: float, passive_income_generated: float) -> None:
        self._goal_data = {
            "total_accumulated": total_accumulated,
            "total_interest": total_interest,
            "total_invested": total_invested,
            "passive_income_generated": passive_income_generated
        }

    def generate_pdf(self, file_name: str) -> None:
        c = canvas.Canvas(file_name, pagesize=letter)
        c.drawString(100, 750, f"Relatório de {self._user.name}")
        c.drawString(100, 730, f"Idade: {self._user.age}")
        c.drawString(100, 710, f"Data de geração: {self._generation_date.strftime('%d/%m/%Y %H:%M:%S')}")

        # Adicione informações de renda
        c.drawString(100, 690, "Renda:")
        y = 670
        for income in self._user._income:
            c.drawString(120, y, f"Tipo: {income.type}, Valor: R$ {income.amount}, Data: {income.date.strftime('%d/%m/%Y')}")
            y -= 20

        # Adicione informações de despesas
        c.drawString(100, y, "Despesas:")
        y -= 20
        for expense in self._user._expenses:
            c.drawString(120, y, f"Tipo: {expense.type}, Valor: R$ {expense.amount}, Data: {expense.date.strftime('%d/%m/%Y')}")
            y -= 20

        # Adicione perfil de investidor
        c.drawString(100, y, "Perfil de Investidor:")
        y -= 20
        if self._user._profile:
            c.drawString(120, y, f"Tipo: {self._user._profile.profile_type}")
            y -= 20
            c.drawString(120, y, f"Descrição: {self._user._profile.description}")
            y -= 20

        # Adicione objetivos e metas
        c.drawString(100, y, "Objetivos:")
        y -= 20
        for objective in self._user._objectives:
            c.drawString(120, y, f"Tipo: {objective.objective_type}, Descrição: {objective.description}")
            y -= 20
            for goal in objective._goals:
                c.drawString(140, y, f"Meta: Aposentar-se aos {goal.retirement_age} anos")
                y -= 20
                c.drawString(140, y, f"Meta de Renda Passiva: R$ {goal.passive_income_goal}")
                y -= 20

        # Adicione os dados da meta financeira
        if self._goal_data:
            c.drawString(100, y, "Dados da Meta Financeira:")
            y -= 20
            c.drawString(120, y, f"Total Acumulado: R$ {self._goal_data['total_accumulated']:.2f}")
            y -= 20
            c.drawString(120, y, f"Total de Juros: R$ {self._goal_data['total_interest']:.2f}")
            y -= 20
            c.drawString(120, y, f"Total Investido: R$ {self._goal_data['total_invested']:.2f}")
            y -= 20
            c.drawString(120, y, f"Renda Passiva Gerada: R$ {self._goal_data['passive_income_generated']:.2f}")
            y -= 20

        c.save()

# Exemplo de endpoint para download do relatório
@app.route('/download_report')
def download_report():
    file_name = "relatorio_usuario.pdf"
    # Gere o PDF com os dados do usuário
    user = User(name="Fulano", age=30)  # Exemplo de usuário, você deve substituir por dados reais
    report = Report(user)
    report.generate_pdf(file_name)

    # Permitir o download do PDF
    return send_file(file_name, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
