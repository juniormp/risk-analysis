from domain.entity.rule.asset.is_house_mortgaged import IsHouseMortgaged
from domain.entity.rule.asset.is_vehicle_produced_last_five_years import VehicleProducedLastFiveYears


class AssetRules:
    def get_rules_list(self):
        return [
            IsHouseMortgaged(),
            VehicleProducedLastFiveYears()
        ]
