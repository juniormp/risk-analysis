from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_score import RiskScore
from domain.entity.rule.Rule import Rule


class HasDependents(Rule):
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__has_dependents(dependents=person.dependents):
            self.__add_points_to(risk_score=risk_profile.get_risk_score())

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __has_dependents(self, dependents: int):
        return dependents > 0

    def __add_points_to(self, risk_score: RiskScore):
        disability = risk_score.get_product_by(risk_score, name='disability')
        disability.add_score_points(1)

        life = risk_score.get_product_by(risk_score, name='life')
        life.add_score_points(1)

