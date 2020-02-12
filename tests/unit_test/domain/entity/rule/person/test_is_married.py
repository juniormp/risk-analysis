from django.test import TestCase
from domain.entity.person import MARITAL_STATUS_SINGLE, MARITAL_STATUS_MARRIED
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.person.is_married import IsMarried
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder


class TestIsMarried(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.person_builder = PersonBuilder()
        self.rule = IsMarried()

    def test_product_score_is_add_in_1_and_deduct_in_1_when_person_is_married(self):
        person = self.person_builder.with_marital_status(MARITAL_STATUS_MARRIED).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(+1, risk_analysis.get_products_in_risk_analysis()['life'].get_score())
        self.assertEqual(-1, risk_analysis.get_products_in_risk_analysis()['disability'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['home'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['vehicle'].get_score())

    def test_product_score_is_not_add_in_1_and_not_deduct_in_1_when_person_is_single(self):
        person = self.person_builder.with_marital_status(MARITAL_STATUS_SINGLE).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['life'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['disability'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['home'].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()['vehicle'].get_score())

