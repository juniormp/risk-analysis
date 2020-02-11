from django.test import TestCase
from domain.entity.house import House
from domain.entity.person import Person
from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE, PRODUCT_SCORE_DEFAULT
from domain.entity.product.vehicle_product import VehicleProduct
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.risk_score import RiskScore
from domain.entity.rule.person.has_asset import HasAsset


class TestHasAsset(TestCase):
    def setUp(self):
        self.home_product = HomeProduct()
        self.vehicle_product = VehicleProduct()
        self.life_product = LifeProduct()
        self.disability_product = DisabilityProduct()
        self.risk_score = RiskScore(
            product={
                'vehicle': self.vehicle_product, 'home': self.home_product,
                'life': self.life_product, 'disability': self.disability_product
            }
        )
        self.risk_profile = RiskProfile(
            risk_score=self.risk_score
        )

    def test_product_score_is_default_when_person_has_no_asset(self):
        rule = HasAsset()
        house = House(
            ownership_status="owned"
        )
        person = Person(
            income=None,
            age=None,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=[house]
        )
        risk_analysis = RiskAnalysis(
            person=person,
            risk_profile=self.risk_profile
        )

        risk_analysis = rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['vehicle'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['home'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['life'].status)
        self.assertEqual(PRODUCT_SCORE_DEFAULT, risk_analysis.risk_profile.risk_score.product['disability'].status)

    def test_product_score_is_ineligible_when_person_has_asset(self):
        rule = HasAsset()
        person = Person(
            income=None,
            age=None,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=[]
        )
        risk_analysis = RiskAnalysis(
            person=person,
            risk_profile=self.risk_profile
        )

        risk_analysis = rule.execute(risk_analysis=risk_analysis)

        self.assertEqual(PRODUCT_SCORE_INELIGIBLE, risk_analysis.risk_profile.risk_score.product['vehicle'].status)
        self.assertEqual(PRODUCT_SCORE_INELIGIBLE, risk_analysis.risk_profile.risk_score.product['home'].status)
        self.assertEqual(PRODUCT_SCORE_INELIGIBLE, risk_analysis.risk_profile.risk_score.product['life'].status)
        self.assertEqual(PRODUCT_SCORE_INELIGIBLE, risk_analysis.risk_profile.risk_score.product['disability'].status)
