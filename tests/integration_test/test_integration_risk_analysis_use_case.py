from django.test import TestCase

from application.use_case.risk_analysis_use_case import RiskAnalysisUseCase
from domain.entity.product.product import HOME_PRODUCT, LIFE_PRODUCT, VEHICLE_PRODUCT, DISABILITY_PRODUCT, \
    PRODUCT_SCORE_ECONOMIC
from risk_analysis.service_registry import ServiceRegistry


class TestIntegrationRiskAnalysisUseCase(TestCase):
    def test_should_execute_risk_analysis_first_simulation(self):
        user_information = {
            "age": 50,
            "dependents": 10,
            "house": {"ownership_status": "owned"},
            "income": 200,
            "marital_status": "married",
            "risk_question": [0, 1, 1],
            "vehicle": {"year": "2018"}
        }

        risk_analysis_use_case = RiskAnalysisUseCase(risk_analysis_service=ServiceRegistry.service_risk_analysis(),
                                                     risk_analysis_rules_factory=ServiceRegistry.factory_risk_analysis_rules(),
                                                     risk_analysis_factory=ServiceRegistry.factory_risk_analysis())

        risk_profile = risk_analysis_use_case.execute(user_information=user_information)

        self.assertEqual(0, risk_profile.get_product_by(HOME_PRODUCT).get_score())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC, risk_profile.get_product_by(HOME_PRODUCT).get_status())

        self.assertEqual(1, risk_profile.get_product_by(VEHICLE_PRODUCT).get_score())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC,
                         risk_profile.get_product_by(VEHICLE_PRODUCT).get_status())

        self.assertEqual(2, risk_profile.get_product_by(LIFE_PRODUCT).get_score())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC, risk_profile.get_product_by(LIFE_PRODUCT).get_status())

        self.assertEqual(0, risk_profile.get_product_by(DISABILITY_PRODUCT).get_score())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC,
                         risk_profile.get_product_by(DISABILITY_PRODUCT).get_status())

    def test_should_execute_risk_analysis_first_simulation_two(self):
        user_information = {
            "age": 35,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 300,
            "marital_status": "married",
            "risk_question": [0, 1, 1],
            "vehicle": {"year": "2018"}
        }

        risk_analysis_use_case = RiskAnalysisUseCase(risk_analysis_service=ServiceRegistry.service_risk_analysis(),
                                                     risk_analysis_rules_factory=ServiceRegistry.factory_risk_analysis_rules(),
                                                     risk_analysis_factory=ServiceRegistry.factory_risk_analysis())

        risk_profile = risk_analysis_use_case.execute(user_information=user_information)

        self.assertEqual(-2, risk_profile.get_product_by(HOME_PRODUCT).get_score())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC,
                         risk_profile.get_product_by(HOME_PRODUCT).get_status())

        self.assertEqual(-1, risk_profile.get_product_by(VEHICLE_PRODUCT).get_score())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC,
                         risk_profile.get_product_by(VEHICLE_PRODUCT).get_status())

        self.assertEqual(0, risk_profile.get_product_by(LIFE_PRODUCT).get_score())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC,
                         risk_profile.get_product_by(LIFE_PRODUCT).get_status())

        self.assertEqual(-2, risk_profile.get_product_by(DISABILITY_PRODUCT).get_score())
        self.assertEqual(PRODUCT_SCORE_ECONOMIC,
                         risk_profile.get_product_by(DISABILITY_PRODUCT).get_status())
