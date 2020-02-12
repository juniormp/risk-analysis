from domain.entity.product.product import DISABILITY_PRODUCT, LIFE_PRODUCT
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.Rule import Rule


class HasDependents(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__has_dependents(dependents=person.dependents):
            self.__add_points_to(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __has_dependents(self, dependents: int):
        return dependents > 0

    def __add_points_to(self, risk_profile: RiskProfile):
        disability = risk_profile.get_product_by(name=DISABILITY_PRODUCT)
        disability.add_score_points(1)

        life = risk_profile.get_product_by(name=LIFE_PRODUCT)
        life.add_score_points(1)

