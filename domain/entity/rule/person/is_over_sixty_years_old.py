from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE, LIFE_PRODUCT, DISABILITY_PRODUCT
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.Rule import Rule


class IsOverSixtyYearsOld(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__is_over_sixty_years_old(age=person.age):
            self.__change_to_ineligible_product_on(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_over_sixty_years_old(self, age: int):
        return age > 60

    def __change_to_ineligible_product_on(self, risk_profile: RiskProfile):
        life = risk_profile.get_product_by(name=LIFE_PRODUCT)
        life.update_status(PRODUCT_SCORE_INELIGIBLE)

        disability = risk_profile.get_product_by(name=DISABILITY_PRODUCT)
        disability.update_status(PRODUCT_SCORE_INELIGIBLE)
