from unittest import TestCase
from unittest.mock import MagicMock
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.asset.is_house_mortgaged import IsHouseMortgaged
from domain.entity.rule.asset.is_vehicle_produced_last_five_years import VehicleProducedLastFiveYears
from domain.entity.rule.person.has_dependents import HasDependents
from domain.entity.rule.person.has_house import HasHouse
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory
from domain.service.risk_analysis_service import RiskAnalysisService


class TestRiskAnalysisService(TestCase):
    def setUp(self):
        self.rule_has_house_mock = MagicMock(autospec=HasHouse)
        self.is_vehicle_produced_last_five_years = MagicMock(autospec=VehicleProducedLastFiveYears)
        self.rule_is_house_mortgaged_mock = MagicMock(autospec=IsHouseMortgaged)
        self.has_dependents = MagicMock(autospec=HasDependents)

        self.person_rules_list = [self.rule_has_house_mock, self.is_vehicle_produced_last_five_years]
        self.asset_rules_list = [self.rule_is_house_mortgaged_mock, self.has_dependents]

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
        risk_analysis_rules_factory_mock = MagicMock(autospec=RiskAnalysisRulesFactory)
        risk_analysis_mock = MagicMock(autospec=RiskAnalysis)
        rules_list_mock = [self.person_rules_list, self.asset_rules_list]
        risk_analysis_service = RiskAnalysisService(
            risk_analysis_rules_factory=risk_analysis_rules_factory_mock
        )

        response = risk_analysis_service.apply_rules_on(rules_list=rules_list_mock,
                                                        risk_analysis=risk_analysis_mock)

        self.rule_has_house_mock.execute.assert_called_once_with(risk_analysis_mock)
        self.is_vehicle_produced_last_five_years.execute.assert_called_once_with(risk_analysis_mock)
        self.rule_is_house_mortgaged_mock.execute.assert_called_once_with(risk_analysis_mock)
        self.has_dependents.execute.assert_called_once_with(risk_analysis_mock)
