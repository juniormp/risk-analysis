from django.test import TestCase
from domain.entity.house import House, OWNERSHIP_STATUS_MORTGAGED, OWNERSHIP_STATUS_OWNED
from domain.entity.rule.asset.is_mortgaged import IsMortgaged


class TestIsMortgaged(TestCase):
    def test_is_truly_when_asset_is_mortgaged(self):
        rule = IsMortgaged()
        house = House(
            ownership_status=OWNERSHIP_STATUS_MORTGAGED
        )

        response = rule.execute(house=house)

        self.assertTrue(response)

    def test_is_falsely_when_asset_is_not_mortgaged(self):
        rule = IsMortgaged()
        house = House(
            ownership_status=OWNERSHIP_STATUS_OWNED
        )

        response = rule.execute(house=house)

        self.assertFalse(response)
