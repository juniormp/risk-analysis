class AssetRules:
    is_house_mortgaged = None
    is_vehicle_produced_las_five_years = None

    def __init__(self, is_house_mortgaged, is_vehicle_produced_las_five_years):
        self.is_house_mortgaged = is_house_mortgaged
        self.is_vehicle_produced_las_five_years = is_vehicle_produced_las_five_years

    def get_rules_list(self):
        return [
            self.is_house_mortgaged,
            self.is_vehicle_produced_las_five_years
        ]
