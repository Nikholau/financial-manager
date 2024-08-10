from user import User

class Report:
    def __init__(self, user: User):
        self._user = user
        self._generation_date = datetime.now()
        self._details = ""

    @property
    def generation_date(self):
        return self._generation_date

    @property
    def details(self):
        return self._details

    def generate(self) -> str:
        # Implementation to generate a report based on the user's data
        pass