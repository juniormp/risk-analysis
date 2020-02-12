from unittest import TestCase
from unittest.mock import MagicMock
from domain.entity.product.status.product_status_builder import ProductStatusBuilder
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.asset.is_house_mortgaged import IsHouseMortgaged
from domain.entity.rule.asset.is_vehicle_produced_last_five_years import VehicleProducedLastFiveYears
from domain.entity.rule.person.has_dependents import HasDependents
from domain.entity.rule.person.has_house import HasHouse
from domain.service.risk_analysis_service import RiskAnalysisService
from tests.risk_profile_builder import RiskProfileBuilder


class TestRiskAnalysisService(TestCase):
    def setUp(self):
        self.rule_has_house_mock = MagicMock(autospec=HasHouse)
        self.is_vehicle_produced_last_five_years = MagicMock(autospec=VehicleProducedLastFiveYears)
        self.rule_is_house_mortgaged_mock = MagicMock(autospec=IsHouseMortgaged)
        self.has_dependents = MagicMock(autospec=HasDependents)

        self.person_rules_list = [self.rule_has_house_mock, self.is_vehicle_produced_last_five_years]
        self.asset_rules_list = [self.rule_is_house_mortgaged_mock, self.has_dependents]

        self.risk_profile = RiskProfileBuilder().with_vehicle_product().with_life_product()\
            .with_home_product().with_disability_product().build()

    def test_execute_risk_analysis_applying_rules_list(self):
        risk_analysis_mock = MagicMock(autospec=RiskAnalysis)
        rules_list_mock = self.person_rules_list + self.asset_rules_list
        product_status_builder = MagicMock(autospec=ProductStatusBuilder)
        risk_analysis_service = RiskAnalysisService(
            product_status_builder=product_status_builder
        )

        risk_analysis_service.apply_rules_on(rules_list=rules_list_mock,
                                             risk_analysis=risk_analysis_mock)

        self.rule_has_house_mock.execute.assert_called_once_with(risk_analysis_mock)
        self.is_vehicle_produced_last_five_years.execute.assert_called_once_with(risk_analysis_mock)
        self.rule_is_house_mortgaged_mock.execute.assert_called_once_with(risk_analysis_mock)
        self.has_dependents.execute.assert_called_once_with(risk_analysis_mock)

    def test_retrieve_risk_score_result(self):
        product_status_builder = ProductStatusBuilder()
        risk_analysis_service = RiskAnalysisService(
            product_status_builder=product_status_builder
        )
        risk_analysis_service.get_result_from(risk_profile=self.risk_profile)




