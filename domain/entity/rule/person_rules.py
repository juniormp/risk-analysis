from domain.entity.rule.person.has_income import HasIncome


class PersonRules:
    has_income = None

    def __init__(self, has_income):
        self.has_income = has_income

    def get_rules_list(self):
        return [self.has_income]
