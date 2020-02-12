from domain.entity.asset import Asset
from domain.entity.house import House
from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE, HOME_PRODUCT
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.Rule import Rule


class HasHouse(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        for asset in person.assets:
            if self.__is_house(asset=asset):
                return risk_analysis

        self.__change_to_ineligible_home_product_on(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_house(self, asset: Asset):
        return type(asset) == House

    def __change_to_ineligible_home_product_on(self, risk_profile: RiskProfile):
        home = risk_profile.get_product_by(name=HOME_PRODUCT)
        home.update_status(PRODUCT_SCORE_INELIGIBLE)
