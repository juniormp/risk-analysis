from domain.entity.rule.person_rules import PersonRules


class RiskAnalysisRulesFactory:
    def __init__(self, person_rules: PersonRules):
        self.person_rules = person_rules

    def create_person_rules(self):
        return self.person_rules.get_rules_list
