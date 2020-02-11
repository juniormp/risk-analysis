from django.test import TestCase
from domain.entity.house import House, OWNERSHIP_STATUS_OWNED
from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE, PRODUCT_SCORE_DEFAULT
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.person.has_house import HasHouse
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder


class TestHasHouse(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.person_builder = PersonBuilder()
        self.person_builder.person.assets = []
        self.rule = HasHouse()

    def test_home_product_status_is_ineligible_when_person_has_no_house(self):
        person = self.person_builder.build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(PRODUCT_SCORE_INELIGIBLE, risk_analysis.risk_profile.risk_score.product['home'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['vehicle'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['disability'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['life'].status)

    def test_home_product_status_is_default_when_person_has_house(self):
        house = House(ownership_status=OWNERSHIP_STATUS_OWNED)
        person = self.person_builder.with_asset(asset=house).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        risk_analysis = self.rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['home'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['vehicle'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['disability'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['life'].status)
