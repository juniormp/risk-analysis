from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE
from domain.entity.product.status.product_status_builder import ProductStatusBuilder
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_score import RiskScore
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory
from array import array


class RiskAnalysisService:
    def __init__(self, risk_analysis_rules_factory: RiskAnalysisRulesFactory,
                 product_status_builder: ProductStatusBuilder):
        self.risk_analysis_rules_factory = risk_analysis_rules_factory
        self.product_status_builder = product_status_builder

    def build_rules_list(self):
        person_rules_list = self.risk_analysis_rules_factory.create_person_rules()
        asset_rules_list = self.risk_analysis_rules_factory.create_asset_rules()
        rules_list = [person_rules_list, asset_rules_list]

        return rules_list

    def apply_rules_on(self, risk_analysis: RiskAnalysis, rules_list: array):
        for rules in rules_list:
            for rule in rules:
                rule.execute(risk_analysis)

    def foo(self, risk_score: RiskScore):
        for key, value in risk_score.products.items():
            for status in self.product_status_builder.build_product_status_list():
                if status.apply_condition(value.score) and value.status != PRODUCT_SCORE_INELIGIBLE:
                    value.update_status(status.name)
