from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE
from domain.entity.risk_analysis import RiskAnalysis


class OverSixtyYearsOld:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if person.age > 60:
            self.__change_to_ineligible_product_on(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __change_to_ineligible_product_on(self, risk_profile):
        life_product = risk_profile.risk_score.product['life']
        life_product.score = PRODUCT_SCORE_INELIGIBLE

        disability = risk_profile.risk_score.product['disability']
        disability.score = PRODUCT_SCORE_INELIGIBLE
