from domain.entity.risk_analysis import RiskAnalysis


class OverSixtyYearsOld:
    def execute(self, risk_analysis: RiskAnalysis):
        person = self.__get_person_from(risk_analysis=risk_analysis)
        if person.age > 60:
            return True

        return False

    def __get_person_from(self, risk_analysis: RiskAnalysis):
        return risk_analysis.person
