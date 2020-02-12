from domain.entity.person import MARITAL_STATUS_MARRIED
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_score import RiskScore
from domain.entity.rule.Rule import Rule


class IsMarried(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__is_married(person.marital_status):
            self.__add_and_deduct_points_from(risk_score=risk_profile.risk_score)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_married(self, marital_status: str):
        return marital_status == MARITAL_STATUS_MARRIED

    def __add_and_deduct_points_from(self, risk_score: RiskScore):
        life = risk_score.get_product_by(risk_score, name='life')
        life.add_score_points(1)

        disability = risk_score.get_product_by(risk_score, name='disability')
        disability.deduct_score_points(1)
