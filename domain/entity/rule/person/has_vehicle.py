from domain.entity.asset import Asset
from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_score import RiskScore
from domain.entity.rule.Rule import Rule
from domain.entity.vehicle import Vehicle


class HasVehicle(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        for asset in person.assets:
            if self.__is_vehicle(asset=asset):
                return risk_analysis

        self.__change_to_ineligible_vehicle_product_on(risk_score=risk_profile.risk_score)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_vehicle(self, asset: Asset):
        return type(asset) == Vehicle

    def __change_to_ineligible_vehicle_product_on(self, risk_score: RiskScore):
        vehicle = risk_score.get_product_by(risk_score, name='vehicle')
        vehicle.update_status(PRODUCT_SCORE_INELIGIBLE)

