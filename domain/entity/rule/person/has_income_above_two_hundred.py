from domain.entity.risk_analysis import RiskAnalysis


class HasIncomeAboveTwoHundred:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__has_income_above_two_hundred(income=person.income):
            self.__deduct_points_from(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __has_income_above_two_hundred(self, income: float):
        return income > 200.00

    def __deduct_points_from(self, risk_profile):
        disability = risk_profile.risk_score.product['disability']
        disability.score = -1

        life = risk_profile.risk_score.product['life']
        life.score = -1

        home = risk_profile.risk_score.product['home']
        home.score = -1

        vehicle = risk_profile.risk_score.product['vehicle']
        vehicle.score = -1

