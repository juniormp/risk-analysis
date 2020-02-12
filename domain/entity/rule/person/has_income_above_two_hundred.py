from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.Rule import Rule
from domain.entity.product.product import DISABILITY_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, VEHICLE_PRODUCT


class HasIncomeAboveTwoHundred(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__has_income_above_two_hundred(income=person.income):
            self.__deduct_points_from(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __has_income_above_two_hundred(self, income: float):
        return income > 200.00

    def __deduct_points_from(self, risk_profile: RiskProfile):
        disability = risk_profile.get_product_by(name=DISABILITY_PRODUCT)
        disability.deduct_score_points(1)

        life = risk_profile.get_product_by(name=LIFE_PRODUCT)
        life.deduct_score_points(1)

        home = risk_profile.get_product_by(name=HOME_PRODUCT)
        home.deduct_score_points(1)

        auto = risk_profile.get_product_by(name=VEHICLE_PRODUCT)
        auto.deduct_score_points(1)



