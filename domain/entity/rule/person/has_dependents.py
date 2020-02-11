from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile


class HasDependents:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__has_dependents(dependents=person.dependents):
            self.__add_points_to(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __has_dependents(self, dependents: int):
        return dependents > 0

    def __add_points_to(self, risk_profile: RiskProfile):
        disability = risk_profile.risk_score.product['disability']
        disability.score = +1

        life = risk_profile.risk_score.product['life']
        life.score = +1
