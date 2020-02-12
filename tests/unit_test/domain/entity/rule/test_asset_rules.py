from django.test import TestCase
from domain.entity.rule.asset.is_house_mortgaged import IsHouseMortgaged
from domain.entity.rule.asset.is_vehicle_produced_last_five_years import VehicleProducedLastFiveYears
from domain.entity.rule.asset_rules import AssetRules


class TestPersonRules(TestCase):
    def setUp(self):
        self.asset_rules_list = [
            IsHouseMortgaged(),
            VehicleProducedLastFiveYears()
        ]

    def test_return_the_list_of_persons_rules(self):
        asset_rules_list = AssetRules()

        response = asset_rules_list.get_rules_list()

        self.assertContains(self.asset_rules_list, response)
