from django.test import TestCase
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.person.under_thirty_years_old import UnderThirtyYearsOld
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder
from domain.entity.product.product import DISABILITY_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, VEHICLE_PRODUCT


class TestUnderThirtyYearsOld(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.person_builder = PersonBuilder()
        self.rule = UnderThirtyYearsOld()

    def test_product_score_is_deduct_in_2_when_person_is_under_thirty_years_old(self):
        person = self.person_builder.with_age(29).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(-2, risk_analysis.get_products_in_risk_analysis()[DISABILITY_PRODUCT].get_score())
        self.assertEqual(-2, risk_analysis.get_products_in_risk_analysis()[HOME_PRODUCT].get_score())
        self.assertEqual(-2, risk_analysis.get_products_in_risk_analysis()[LIFE_PRODUCT].get_score())
        self.assertEqual(-2, risk_analysis.get_products_in_risk_analysis()[VEHICLE_PRODUCT].get_score())

    def test_product_score_is_not_deduct_in_2_when_person_is_over_thirty_years_old(self):
        person = self.person_builder.with_age(30).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[DISABILITY_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[HOME_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[LIFE_PRODUCT].get_score())
        self.assertEqual(0, risk_analysis.get_products_in_risk_analysis()[VEHICLE_PRODUCT].get_score())
