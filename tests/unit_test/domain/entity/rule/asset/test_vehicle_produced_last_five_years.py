from django.test import TestCase
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.asset.is_vehicle_produced_last_five_years import VehicleProducedLastFiveYears
from domain.entity.product.product import DISABILITY_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, VEHICLE_PRODUCT
from domain.entity.vehicle import Vehicle
from freezegun import freeze_time
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder


class TestVehicleProducedLastFiveYears(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.person_builder = PersonBuilder()
        self.rule = VehicleProducedLastFiveYears()

    @freeze_time("2020-01-01")
    def test_product_score_is_add_in_1_when_vehicle_was_produced_last_5_years(self):
        vehicle = Vehicle(year_manufactured=2015)
        person = self.person_builder.with_asset(asset=vehicle).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(+1, risk_analysis.get_products_in_risk_analysis()[VEHICLE_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[DISABILITY_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[HOME_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[LIFE_PRODUCT].get_score())

    @freeze_time("2020-01-01")
    def test_product_score_is_not_add_in_1_when_vehicle_was_produced_last_5_years(self):
        vehicle = Vehicle(year_manufactured=2013)
        self.person_builder.person.assets = []
        person = self.person_builder.with_asset(asset=vehicle).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[DISABILITY_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[HOME_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[LIFE_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[VEHICLE_PRODUCT].get_score())
