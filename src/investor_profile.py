class InvestorProfile:
    def __init__(self, profile_type: str, description: str):
        self._profile_type = profile_type
        self._description = description

    @property
    def profile_type(self):
        return self._profile_type

    @property
    def description(self):
        return self._description