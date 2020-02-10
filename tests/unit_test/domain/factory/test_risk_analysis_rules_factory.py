from unittest import TestCase
from unittest.mock import MagicMock
from domain.entity.rule.person_rules import PersonRules
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory


class TestRiskAnalysisRulesFactory(TestCase):
    def test_retrieve_persons_rules_list(self):
        person_rules_expected = ['fake_person_rules']
        person_rules_mock = MagicMock(autospec=PersonRules)
        risk_analysis_rules_factory = RiskAnalysisRulesFactory(person_rules=person_rules_mock)
        person_rules_mock.get_rules_list.return_value = person_rules_expected

        response = risk_analysis_rules_factory.create_person_rules()

        self.assertEqual(person_rules_expected, response.return_value)

