from goal import Goal

class Objective:
    def __init__(self, objective_type: str, description: str):
        self._objective_type = objective_type
        self._description = description
        self._goals = []

    @property
    def objective_type(self):
        return self._objective_type

    @objective_type.setter
    def objective_type(self, value: str):
        self._objective_type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    def add_goal(self, goal: Goal) -> None:
        self._goals.append(goal)

    def calculate_total_annual(self) -> float:
        pass
