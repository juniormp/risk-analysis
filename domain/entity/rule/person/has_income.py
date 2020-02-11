from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE
from domain.entity.risk_analysis import RiskAnalysis


class HasIncome:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if person.income <= 0:
            self.__change_to_ineligible_product_on(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __change_to_ineligible_product_on(self, risk_profile):
        life_product = risk_profile.risk_score.product['disability']
        life_product.status = PRODUCT_SCORE_INELIGIBLE
