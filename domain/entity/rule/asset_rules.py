class AssetRules:
    is_mortgaged = None

    def __init__(self, is_mortgaged):
        self.is_mortgaged = is_mortgaged

    def get_rules_list(self):
        return [
            self.is_mortgaged
        ]
