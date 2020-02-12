from domain.entity.person import Person
from domain.entity.risk_profile import RiskProfile


class RiskAnalysis:
    person: Person
    risk_profile: RiskProfile

    def __init__(self, person: Person, risk_profile: RiskProfile):
        self.person = person
        self.risk_profile = risk_profile

    def get_products_in_risk_analysis(self):
        return self.risk_profile.get_products()

    def __eq__(self, other):
        return isinstance(other, RiskAnalysis) and \
               other.person == self.person and \
               other.risk_profile == self.risk_profile
