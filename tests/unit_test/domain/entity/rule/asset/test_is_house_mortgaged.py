from django.test import TestCase
from domain.entity.house import House, OWNERSHIP_STATUS_MORTGAGED, OWNERSHIP_STATUS_OWNED
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.asset.is_house_mortgaged import IsHouseMortgaged
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder


class TestIsHouseMortgaged(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.person_builder = PersonBuilder()
        self.rule = IsHouseMortgaged()

    def test_product_score_is_add_in_1_when_house_is_mortgaged(self):
        house = House(ownership_status=OWNERSHIP_STATUS_MORTGAGED)
        person = self.person_builder.with_asset(asset=house).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(+1, risk_analysis.get_products_in_risk_analysis()['disability'].get_score())
        self.assertEqual(+1, risk_analysis.get_products_in_risk_analysis()['home'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['life'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['vehicle'].get_score())

    def test_product_score_remains_in_0_when_house_is_not_mortgaged(self):
        house = House(ownership_status=OWNERSHIP_STATUS_OWNED)
        self.person_builder.person.assets = []
        person = self.person_builder.with_asset(asset=house).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['disability'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['home'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['life'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['vehicle'].get_score())
