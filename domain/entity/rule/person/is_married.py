from domain.entity.person import MARITAL_STATUS_MARRIED
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile


class IsMarried:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__is_married(person.marital_status):
            self.__add_and_deduct_points_from(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_married(self, marital_status: str):
        return marital_status == MARITAL_STATUS_MARRIED

    def __add_and_deduct_points_from(self, risk_profile: RiskProfile):
        life = risk_profile.risk_score.product['life']
        life.score = +1

        disability = risk_profile.risk_score.product['disability']
        disability.score = -1
