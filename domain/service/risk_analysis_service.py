from array import array

from domain.entity.product.product import Product, PRODUCT_SCORE_INELIGIBLE
from domain.entity.risk_analysis import RiskAnalysis
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory


class RiskAnalysisService:
    def __init__(self, risk_analysis_rules_factory: RiskAnalysisRulesFactory):
        self.risk_analysis_rules_factory = risk_analysis_rules_factory

    def build_rules_list(self):
        person_rules_list = self.risk_analysis_rules_factory.create_person_rules()
        asset_rules_list = self.risk_analysis_rules_factory.create_asset_rules()
        rules_list = [person_rules_list, asset_rules_list]

        return rules_list

    def apply_rules_on(self, risk_analysis: RiskAnalysis, rules_list: array):
        for rules in rules_list:
            for rule in rules:
                rule.execute(risk_analysis)


    def get_risk_analysis_result_from(self, products: dict):
        for product_name, product in products:
            if product.status != PRODUCT_SCORE_INELIGIBLE:
                pro



