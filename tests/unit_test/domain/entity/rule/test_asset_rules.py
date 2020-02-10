from django.test import TestCase
from domain.entity.rule.asset.is_house_mortgaged import IsHouseMortgaged
from domain.entity.rule.asset.is_vehicle_produced_last_five_years import VehicleProducedLastFiveYears
from domain.entity.rule.asset_rules import AssetRules


class TestPersonRules(TestCase):
    def setUp(self):
        self.is_house_mortgaged = IsHouseMortgaged()
        self.is_vehicle_produced_las_five_years = VehicleProducedLastFiveYears()
        self.asset_rules_list = [
            self.is_house_mortgaged,
            self.is_vehicle_produced_las_five_years
        ]

    def test_return_the_list_of_persons_rules(self):
        asset_rules_list = AssetRules(
            self.is_house_mortgaged,
            self.is_vehicle_produced_las_five_years
        )

        response = asset_rules_list.get_rules_list()

        self.assertEqual(self.asset_rules_list, response)
