from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_score import RiskScore


class BetweenThirtyAndFortyYearsOld:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__is_between_thirty_and_forty_years_old(age=person.age):
            self.__deduct_points_from(risk_score=risk_profile.get_risk_score())

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_between_thirty_and_forty_years_old(self, age: int):
        return all([age >= 30, age <= 40])

    def __deduct_points_from(self, risk_score: RiskScore):
        disability = risk_score.get_product_by(risk_score, name='disability')
        disability.deduct_score_points(1)

        life = risk_score.get_product_by(risk_score, name='life')
        life.deduct_score_points(1)

        home = risk_score.get_product_by(risk_score, name='home')
        home.deduct_score_points(1)

        auto = risk_score.get_product_by(risk_score, name='vehicle')
        auto.deduct_score_points(1)