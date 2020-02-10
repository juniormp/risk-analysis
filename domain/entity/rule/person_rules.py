class PersonRules:
    has_income = None
    has_asset = None
    over_sixty_years_old = None
    under_thirty_years_old = None

    def __init__(self, has_income, has_asset, over_sixty_years_old, under_thirty_years_old):
        self.has_income = has_income
        self.has_asset = has_asset
        self.over_sixty_years_old = over_sixty_years_old
        self.under_thirty_years_old = under_thirty_years_old

    def get_rules_list(self):
        return [
            self.has_income,
            self.has_asset,
            self.over_sixty_years_old,
            self.under_thirty_years_old
        ]
