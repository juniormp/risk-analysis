from domain.entity.risk_analysis import RiskAnalysis


class BetweenThirtyAndFortyYearsOld:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        conditions = [person.age >= 30, person.age <= 40]
        if all(conditions):
            self.__deduct_points_from(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __deduct_points_from(self, risk_profile):
        life_product = risk_profile.risk_score.product['life']
        life_product.score = -1

        disability = risk_profile.risk_score.product['disability']
        disability.score = -1

        life_product = risk_profile.risk_score.product['home']
        life_product.score = -1

        disability = risk_profile.risk_score.product['vehicle']
        disability.score = -1
