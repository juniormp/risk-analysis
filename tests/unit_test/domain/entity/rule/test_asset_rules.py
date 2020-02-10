from django.test import TestCase
from domain.entity.rule.asset.is_mortgaged import IsMortgaged
from domain.entity.rule.asset_rules import AssetRules


class TestPersonRules(TestCase):
    def setUp(self):
        self.is_mortgaged = IsMortgaged()
        self.asset_rules_list = [
            self.is_mortgaged
        ]

    def test_return_the_list_of_persons_rules(self):
        asset_rules_list = AssetRules(
            self.is_mortgaged
        )

        response = asset_rules_list.get_rules_list()

        self.assertEqual(self.asset_rules_list, response)
