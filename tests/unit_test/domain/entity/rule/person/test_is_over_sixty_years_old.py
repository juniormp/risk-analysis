from django.test import TestCase
from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE, PRODUCT_SCORE_ECONOMIC
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.person.is_over_sixty_years_old import IsOverSixtyYearsOld
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder
from domain.entity.product.product import DISABILITY_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, VEHICLE_PRODUCT


class TestIsOverSixtyYearsOld(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.person_builder = PersonBuilder()
        self.rule = IsOverSixtyYearsOld()

    def test_product_score_is_ineligible_when_person_is_over_sixty_years_old(self):
        person = self.person_builder.with_age(61).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile, rules_list=None)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(PRODUCT_SCORE_ECONOMIC, risk_analysis.get_products_in_risk_analysis()[HOME_PRODUCT].get_status())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC, risk_analysis.get_products_in_risk_analysis()[VEHICLE_PRODUCT].get_status())
        self.assertEqual(PRODUCT_SCORE_INELIGIBLE, risk_analysis.get_products_in_risk_analysis()[LIFE_PRODUCT].get_status())
        self.assertEqual(PRODUCT_SCORE_INELIGIBLE, risk_analysis.get_products_in_risk_analysis()[DISABILITY_PRODUCT].get_status())

    def test_product_score_is_default_when_person_is_under_sixty_years_old(self):
        person = self.person_builder.with_age(60).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile, rules_list=None)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(PRODUCT_SCORE_ECONOMIC, risk_analysis.get_products_in_risk_analysis()[HOME_PRODUCT].get_status())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC, risk_analysis.get_products_in_risk_analysis()[VEHICLE_PRODUCT].get_status())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC, risk_analysis.get_products_in_risk_analysis()[LIFE_PRODUCT].get_status())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC, risk_analysis.get_products_in_risk_analysis()[DISABILITY_PRODUCT].get_status())
