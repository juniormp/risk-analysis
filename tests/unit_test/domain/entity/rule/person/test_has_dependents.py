from django.test import TestCase
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.person.has_dependents import HasDependents
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder
from domain.entity.product.product import DISABILITY_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, VEHICLE_PRODUCT


class TestHasDependents(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.person_builder = PersonBuilder()
        self.rule = HasDependents()

    def test_product_score_is_add_in_1_when_person_has_dependents(self):
        person = self.person_builder.with_dependents(1).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(+1, risk_analysis.get_products_in_risk_analysis()[DISABILITY_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[HOME_PRODUCT].get_score())
        self.assertEqual(+1, risk_analysis.get_products_in_risk_analysis()[LIFE_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[VEHICLE_PRODUCT].get_score())

    def test_product_score_is_not_add_in_1_when_person_has_not_dependents(self):
        person = self.person_builder.with_dependents(0).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[DISABILITY_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[HOME_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[LIFE_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[VEHICLE_PRODUCT].get_score())
