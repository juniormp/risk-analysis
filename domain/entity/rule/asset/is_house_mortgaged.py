from domain.entity.house import House, OWNERSHIP_STATUS_MORTGAGED
from domain.entity.risk_analysis import RiskAnalysis


class IsHouseMortgaged:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        for asset in person.assets:
            if type(asset) == House:
                if asset.ownership_status == OWNERSHIP_STATUS_MORTGAGED:
                    self.__add_points_to(risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __add_points_to(self, risk_profile):
        disability = risk_profile.risk_score.product['disability']
        disability.score = +1

        life_product = risk_profile.risk_score.product['home']
        life_product.score = +1
