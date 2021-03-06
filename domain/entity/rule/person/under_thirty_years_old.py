from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.product.product import DISABILITY_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, VEHICLE_PRODUCT
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.Rule import Rule


class UnderThirtyYearsOld(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__is_under_thirty_years_old(age=person.age):
            self.__deduct_points_from(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_under_thirty_years_old(self, age: int):
        return age < 30

    def __deduct_points_from(self, risk_profile: RiskProfile):
        disability = risk_profile.get_product_by(name=DISABILITY_PRODUCT)
        disability.deduct_score_points(2)

        life = risk_profile.get_product_by(name=LIFE_PRODUCT)
        life.deduct_score_points(2)

        home = risk_profile.get_product_by(name=HOME_PRODUCT)
        home.deduct_score_points(2)

        auto = risk_profile.get_product_by(name=VEHICLE_PRODUCT)
        auto.deduct_score_points(2)
