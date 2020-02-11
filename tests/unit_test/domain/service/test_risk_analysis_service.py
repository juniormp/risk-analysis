from unittest import TestCase
from unittest.mock import MagicMock
from domain.entity.house import House, OWNERSHIP_STATUS_OWNED
from domain.entity.person import Person, MARITAL_STATUS_SINGLE
from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.product.vehicle_product import VehicleProduct
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.risk_score import RiskScore
from domain.entity.rule.asset.is_house_mortgaged import IsHouseMortgaged
from domain.entity.rule.person.has_asset import HasAsset
from domain.entity.vehicle import Vehicle
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory
from domain.service.risk_analysis_service import RiskAnalysisService


class TestRiskAnalysisService(TestCase):
    def setUp(self):
        self.house = House(ownership_status=OWNERSHIP_STATUS_OWNED)
        self.vehicle = Vehicle(year_manufactured=2015)
        self.person = Person(
            age=28,
            dependents=1,
            income=100,
            marital_status=MARITAL_STATUS_SINGLE,
            risk_question=[False, True, True],
            assets=[self.house, self.vehicle]
        )
        self.home_product = HomeProduct()
        self.life_product = LifeProduct()
        self.vehicle_product = VehicleProduct()
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

    def test_should_build_rules_list(self):
        person_rules_list_fake = ['person_rules_list_fake']
        asset_rules_list_fake = ['asset_rules_list_fake']
        risk_analysis_rules_factory_mock = MagicMock(autospec=RiskAnalysisRulesFactory)
        risk_analysis_service = RiskAnalysisService(
            risk_analysis_rules_factory=risk_analysis_rules_factory_mock
        )
        risk_analysis_rules_factory_mock.create_person_rules.return_value = person_rules_list_fake
        risk_analysis_rules_factory_mock.create_asset_rules.return_value = asset_rules_list_fake

        rules_list = risk_analysis_service.build_rules_list()

        self.assertEqual([person_rules_list_fake, asset_rules_list_fake], rules_list)

    def test_execute_risk_analysis_using_rules_list(self):
        rule_has_asset_mock = MagicMock(autospec=HasAsset)
        rule_is_house_mortgaged_mock = MagicMock(autospec=IsHouseMortgaged)
        person_rules_list = [rule_has_asset_mock]
        asset_rules_list = [rule_is_house_mortgaged_mock]
        risk_analysis_rules_factory_mock = MagicMock(autospec=RiskAnalysisRulesFactory)
        risk_analysis_service = RiskAnalysisService(
            risk_analysis_rules_factory=risk_analysis_rules_factory_mock
        )

        risk_analysis_service.apply_rules_on(rules_list=[person_rules_list, asset_rules_list], risk_analysis=self.risk_analysis)

        rule_has_asset_mock.execute.assert_called_once_with(self.risk_analysis)
        rule_is_house_mortgaged_mock.execute.assert_called_once_with(self.risk_analysis)
