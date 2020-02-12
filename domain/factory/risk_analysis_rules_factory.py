from domain.entity.rule.asset_rules import AssetRules
from domain.entity.rule.person_rules import PersonRules


class RiskAnalysisRulesFactory:
    def __init__(self, person_rules: PersonRules, asset_rules: AssetRules):
        self.person_rules = person_rules
        self.asset_rules = asset_rules

    def create_person_rules(self):
        return self.person_rules.get_rules_list()

    def create_asset_rules(self):
        return self.asset_rules.get_rules_list()
