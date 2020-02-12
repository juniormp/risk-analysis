from domain.entity.person import MARITAL_STATUS_MARRIED
from domain.entity.product.product import DISABILITY_PRODUCT, LIFE_PRODUCT
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.Rule import Rule


class IsMarried(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__is_married(person.marital_status):
            self.__add_and_deduct_points_from(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_married(self, marital_status: str):
        return marital_status == MARITAL_STATUS_MARRIED

    def __add_and_deduct_points_from(self, risk_profile: RiskProfile):
        life = risk_profile.get_product_by(name=LIFE_PRODUCT)
        life.add_score_points(1)

        disability = risk_profile.get_product_by(name=DISABILITY_PRODUCT)
        disability.deduct_score_points(1)
