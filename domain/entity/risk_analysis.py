import array

from domain.entity.person import Person
from domain.entity.risk_profile import RiskProfile


class RiskAnalysis:
    person: Person
    risk_profile: RiskProfile
    rules_list: array

    def __init__(self, person: Person, risk_profile: RiskProfile, rules_list: array):
        self.person = person
        self.risk_profile = risk_profile
        self.rules_list = rules_list

    def get_products_in_risk_analysis(self):
        return self.risk_profile.get_products()

    def get_rules_list(self):
        return self.rules_list

    def __eq__(self, other):
        return isinstance(other, RiskAnalysis) and \
               other.person == self.person and \
               other.risk_profile == self.risk_profile
