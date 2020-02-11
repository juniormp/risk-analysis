from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.Rule import Rule


class HasAsset(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        for asset in person.assets:
            return risk_analysis

        vehicle_product = risk_profile.risk_score.product['vehicle']
        vehicle_product.score = PRODUCT_SCORE_INELIGIBLE

        home_product = risk_profile.risk_score.product['home']
        home_product.score = PRODUCT_SCORE_INELIGIBLE

        life_product = risk_profile.risk_score.product['life']
        life_product.score = PRODUCT_SCORE_INELIGIBLE

        disability = risk_profile.risk_score.product['disability']
        disability.score = PRODUCT_SCORE_INELIGIBLE

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile
