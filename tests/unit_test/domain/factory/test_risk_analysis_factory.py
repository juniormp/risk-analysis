from django.test import TestCase

from domain.entity.house import House
from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.risk_score import RiskScore
from domain.entity.vehicle import Vehicle
from domain.entity.product.vehicle_product import VehicleProduct
from domain.factory.risk_analysis_factory import RiskAnalysisFactory
from domain.entity.person import Person


class TestRiskAnalysisFactory(TestCase):
    def setUp(self):
        self.user_profile_information = {
            'age': 30,
            'dependents': 0,
            'income': 100,
            'marital_status': 'married',
            'risk_question': [False, True, True],
            'ownership_status': 'owned',
            'year_manufactured': 2018
        }

        self.house = House(ownership_status="owned")
        self.vehicle = Vehicle(year_manufactured=2018)
        self.person = Person(
            age=30,
            dependents=0,
            income=100,
            marital_status='married',
            risk_question=[False, True, True],
            assets=[self.house, self.vehicle]
        )
        self.vehicle_product = VehicleProduct()
        self.home_product = HomeProduct()
        self.life_product = LifeProduct()
        self.disability_product = DisabilityProduct()
        self.risk_score = RiskScore(
            product=[self.vehicle_product, self.home_product, self.life_product, self.disability_product]
        )
        self.risk_profile = RiskProfile(
            risk_score=self.risk_score
        )
        self.risk_analysis = RiskAnalysis(
            person=self.person,
            risk_profile=self.risk_profile
        )

    def test_create_risk_analysis(self):
        risk_analysis_factory = RiskAnalysisFactory()

        response = risk_analysis_factory.createRiskAnalysis(self.user_profile_information)

        self.assertEqual(self.risk_analysis, response)
