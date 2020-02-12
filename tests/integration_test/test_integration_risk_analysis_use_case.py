from django.test import TestCase

from application.use_case.risk_analysis_use_case import RiskAnalysisUseCase
from risk_analysis.service_registry import ServiceRegistry


class TestIntegrationRiskAnalysisUseCase(TestCase):
    def setUp(self):
        self.user_information = {
            "age": 50,
            "dependents": 10,
            "ownership_status": "owned",
            "income": 200,
            "marital_status": "married",
            "risk_question": [0, 1, 1],
            "year_manufactured": 2015
        }

    def test_foo(self):
        risk_analysis_use_case = RiskAnalysisUseCase(risk_analysis_service=ServiceRegistry.service_risk_analysis(),
                                                     risk_analysis_rules_factory=ServiceRegistry.factory_risk_analysis_rules(),
                                                     risk_analysis_factory=ServiceRegistry.factory_risk_analysis())

        risk_analysis = risk_analysis_use_case.execute(user_information=self.user_information)
