from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile


class HasDependents:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if person.dependents > 0:
            self.__add_points_to(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __add_points_to(self, risk_profile: RiskProfile):
        life_product = risk_profile.risk_score.product['disability']
        life_product.score = +1

        life_product = risk_profile.risk_score.product['life']
        life_product.score = +1
