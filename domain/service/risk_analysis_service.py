from domain.entity.risk_analysis import RiskAnalysis


class RiskAnalysisService:
    risk_analysis_rules_factory = None

    def __init__(self, risk_analysis_rules_factory):
        self.risk_analysis_rules_factory = risk_analysis_rules_factory.create_person_rules_to_apply

    def create_risk_analysis(self, risk_analysis=RiskAnalysis):
        person_rules = self.risk_analysis_rules_factory.create_person_rules_to_apply(risk_analysis)
        rules_list = [person_rules]

        return self.__apply_rules_on(rules_list)

    def __apply_rules_on(self, rules_list):
        for rule in rules_list:
            print(rule)
