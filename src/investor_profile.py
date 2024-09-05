class InvestorProfile:
    def __init__(self, profile_type: str):
        self._profile_type = profile_type

    @property
    def profile_type(self):
        return self._profile_type

    @profile_type.setter
    def profile_type(self, value: str):
        self._profile_type = value

