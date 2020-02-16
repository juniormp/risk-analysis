from django.test import TestCase
from domain.entity.house import House
from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.product.product import VEHICLE_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, DISABILITY_PRODUCT
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.asset_rules import AssetRules
from domain.entity.rule.person_rules import PersonRules
from domain.entity.vehicle import Vehicle
from domain.entity.product.vehicle_product import VehicleProduct
from domain.factory.risk_analysis_factory import RiskAnalysisFactory
from domain.entity.person import Person
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory


class TestRiskAnalysisFactory(TestCase):
    def setUp(self):
        self.user_profile_information = {
            'age': 30,
            'dependents': 0,
            'income': 100,
            'marital_status': 'married',
            'risk_question': [False, True, True],
            'house': {'ownership_status': 'owned'},
            'vehicle': {'year': '2018'}
        }

        self.rules_list = RiskAnalysisRulesFactory(PersonRules(), AssetRules()).build_rules_list()
        self.house = House(ownership_status=self.user_profile_information['house']['ownership_status'])
        self.vehicle = Vehicle(year_manufactured=self.user_profile_information['vehicle']['year'])
        self.person = Person(
            age=self.user_profile_information['age'],
            dependents=self.user_profile_information['dependents'],
            income=self.user_profile_information['income'],
            marital_status=self.user_profile_information['marital_status'],
            risk_question=self.user_profile_information['risk_question'],
            assets=[self.house, self.vehicle]
        )
        self.vehicle_product = VehicleProduct()
        self.home_product = HomeProduct()
        self.life_product = LifeProduct()
        self.disability_product = DisabilityProduct()

        self.risk_profile = RiskProfile(
            products={
                VEHICLE_PRODUCT: self.vehicle_product,
                HOME_PRODUCT: self.home_product,
                LIFE_PRODUCT: self.life_product,
                DISABILITY_PRODUCT: self.disability_product
            },
        )
        self.risk_analysis = RiskAnalysis(
            person=self.person,
            risk_profile=self.risk_profile,
            rules_list=self.rules_list
        )

    def test_create_risk_analysis(self):
        risk_analysis_factory = RiskAnalysisFactory()

        response = risk_analysis_factory.create_risk_analysis_from(self.user_profile_information)

        self.assertEqual(self.risk_analysis, response)
