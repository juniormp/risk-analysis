from domain.entity.asset import Asset
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.Rule import Rule
from domain.entity.vehicle import Vehicle
import pendulum


class VehicleProducedLastFiveYears(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        for asset in person.assets:
            if self.__is_vehicle(asset=asset) and self.__was_produced_last_five_years(asset.year_manufactured):
                self.__add_points_to(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_vehicle(self, asset: Asset):
        return type(asset) == Vehicle

    def __was_produced_last_five_years(self, year_manufactured: pendulum.datetime):
        time_right_now = pendulum.now()
        five_years_ago = time_right_now.subtract(years=5)

        return year_manufactured.year > five_years_ago.year

    def __add_points_to(self, risk_profile: RiskProfile):
        auto = risk_profile.get_product_by(name='vehicle')
        auto.add_score_points(1)

