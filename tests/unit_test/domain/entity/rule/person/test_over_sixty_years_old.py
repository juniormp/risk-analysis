from django.test import TestCase
from domain.entity.person import Person
from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.product.vehicle_product import VehicleProduct
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.risk_score import RiskScore
from domain.entity.rule.person.over_sixty_years_old import OverSixtyYearsOld


class TestOverSixtyYearsOld(TestCase):
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

    def test_is_truly_when_person_is_over_sixty_years_old(self):
        rule = OverSixtyYearsOld()
        person = Person(
            income=None,
            age=61,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )
        risk_analysis = RiskAnalysis(
            person=person,
            risk_profile=self.risk_profile
        )

        response = rule.execute(risk_analysis=risk_analysis)

        self.assertTrue(response)

    def test_is_falsely_when_person_under_sixty_years_old(self):
        rule = OverSixtyYearsOld()
        person = Person(
            income=None,
            age=60,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )
        risk_analysis = RiskAnalysis(
            person=person,
            risk_profile=self.risk_profile
        )

        response = rule.execute(risk_analysis=risk_analysis)

        self.assertFalse(response)
