from domain.entity.risk_analysis import RiskAnalysis


class BetweenThirtyAndFortyYearsOld:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        risk_profile = self.__get_risk_profile_from(risk_analysis=risk_analysis)

        if self.__is_between_thirty_and_forty_years_old(age=person.age):
            self.__deduct_points_from(risk_profile=risk_profile)

        return risk_analysis

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person

    def __get_risk_profile_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.risk_profile

    def __is_between_thirty_and_forty_years_old(self, age: int):
        return all([age >= 30, age <= 40])

    def __deduct_points_from(self, risk_profile):
        life_product = risk_profile.risk_score.product['life']
        life_product.score = -1

        disability = risk_profile.risk_score.product['disability']
        disability.score = -1

        home_product = risk_profile.risk_score.product['home']
        home_product.score = -1

        vehicle = risk_profile.risk_score.product['vehicle']
        vehicle.score = -1
