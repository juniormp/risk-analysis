class AssetRules:
    is_mortgaged = None

    def __init__(self, is_mortgaged, is_vehicle_produced_las_five_years):
        self.is_mortgaged = is_mortgaged
        self.is_vehicle_produced_las_five_years = is_vehicle_produced_las_five_years

    def get_rules_list(self):
        return [
            self.is_mortgaged,
            self.is_vehicle_produced_las_five_years
        ]
