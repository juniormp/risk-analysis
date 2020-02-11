from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.vehicle import Vehicle
import pendulum


class VehicleProducedLastFiveYears:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)
        time_right_now = pendulum.now()
        five_years_ago = time_right_now.subtract(years=5)

        for asset in person.assets:
            if type(asset) == Vehicle:
                if asset.year_manufactured.year > five_years_ago.year:
                    self.__add_points_to(risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __add_points_to(self, risk_profile):
        vehicle = risk_profile.risk_score.product['vehicle']
        vehicle.score = +1
