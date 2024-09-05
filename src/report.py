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

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value: User):
        self._user = value

    @property
    def generation_date(self):
        return self._generation_date

    @generation_date.setter
    def generation_date(self, value: datetime):
        self._generation_date = value

    @property
    def goal_data(self):
        return self._goal_data

    @goal_data.setter
    def goal_data(self, value: dict):
        self._goal_data = value

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

        c.drawString(100, 690, "Renda:")
        y = 670
        for income in self._user._income:
            c.drawString(120, y, f"Tipo: {income.type}, Valor: R$ {income.amount}, Data: {income.date.strftime('%d/%m/%Y')}")
            y -= 20

        c.drawString(100, y, "Despesas:")
        y -= 20
        for expense in self._user._expenses:
            c.drawString(120, y, f"Tipo: {expense.type}, Valor: R$ {expense.amount}, Data: {expense.date.strftime('%d/%m/%Y')}")
            y -= 20

        c.drawString(100, y, "Perfil de Investidor:")
        y -= 20
        if self._user._profile:
            c.drawString(120, y, f"Tipo: {self._user._profile.profile_type}")
            y -= 20
            c.drawString(120, y, f"Descrição: {self._user._profile.description}")
            y -= 20

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


if __name__ == "__main__":
    app.run(debug=True)
