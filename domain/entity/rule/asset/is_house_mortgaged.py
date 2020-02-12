from domain.entity.asset import Asset
from domain.entity.house import House, OWNERSHIP_STATUS_MORTGAGED
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_score import RiskScore
from domain.entity.rule.Rule import Rule


class IsHouseMortgaged(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        for asset in person.assets:
            if self.__is_house(asset=asset) and self.is_house_mortgaged(ownership_status=asset.ownership_status):
                self.__add_points_to(risk_score=risk_profile.get_risk_score())

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_house(self, asset: Asset):
        return type(asset) == House

    def is_house_mortgaged(self, ownership_status: str):
        return ownership_status == OWNERSHIP_STATUS_MORTGAGED

    def __add_points_to(self, risk_score: RiskScore):
        disability = risk_score.get_product_by(risk_score, name='disability')
        disability.add_score_points(1)

        home = risk_score.get_product_by(risk_score, name='home')
        home.add_score_points(1)
