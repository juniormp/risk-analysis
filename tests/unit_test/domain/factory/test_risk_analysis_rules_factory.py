from unittest import TestCase
from unittest.mock import MagicMock
from domain.entity.rule.asset_rules import AssetRules
from domain.entity.rule.person_rules import PersonRules
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory


class TestRiskAnalysisRulesFactory(TestCase):
    def test_retrieve_person_rules_list(self):
        person_rules_expected = ['fake_person_rules']
        person_rules_mock = MagicMock(autospec=PersonRules)
        asset_rules_mock = MagicMock(autospec=AssetRules)
        risk_analysis_rules_factory = RiskAnalysisRulesFactory(
            person_rules=person_rules_mock,
            asset_rules=asset_rules_mock
        )
        person_rules_mock.get_rules_list.return_value = person_rules_expected

        response = risk_analysis_rules_factory.create_person_rules()

        self.assertEqual(person_rules_expected, response)

    def test_retrieve_asset_rules_list(self):
        asset_rules_expected = ['fake_asset_rules']
        person_rules_mock = MagicMock(autospec=PersonRules)
        asset_rules_mock = MagicMock(autospec=AssetRules)
        risk_analysis_rules_factory = RiskAnalysisRulesFactory(
            person_rules=person_rules_mock,
            asset_rules=asset_rules_mock
        )
        asset_rules_mock.get_rules_list.return_value = asset_rules_expected

        response = risk_analysis_rules_factory.create_asset_rules()

        self.assertEqual(asset_rules_expected, response)

