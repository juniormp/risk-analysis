from domain.entity.asset import Asset
from domain.entity.house import House, OWNERSHIP_STATUS_MORTGAGED
from domain.entity.product.product import DISABILITY_PRODUCT, HOME_PRODUCT
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.Rule import Rule


class IsHouseMortgaged(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        for asset in person.assets:
            if self.__is_house(asset=asset) and self.is_house_mortgaged(ownership_status=asset.ownership_status):
                self.__add_points_to(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_house(self, asset: Asset):
        return type(asset) == House

    def is_house_mortgaged(self, ownership_status: str):
        return ownership_status == OWNERSHIP_STATUS_MORTGAGED

    def __add_points_to(self, risk_profile: RiskProfile):
        disability = risk_profile.get_product_by(name=DISABILITY_PRODUCT)
        disability.add_score_points(1)

        home = risk_profile.get_product_by(name=HOME_PRODUCT)
        home.add_score_points(1)
