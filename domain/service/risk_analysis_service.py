from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE
from domain.entity.product.status.product_status_builder import ProductStatusBuilder
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_score import RiskScore
from array import array


class RiskAnalysisService:
    def __init__(self, product_status_builder: ProductStatusBuilder):
        self.product_status_builder = product_status_builder

    def apply_rules_on(self, risk_analysis: RiskAnalysis, rules_list: array):
        for rule in rules_list:
            rule.execute(risk_analysis)

    def execute_risk_analysis(self, risk_score: RiskScore):
        for __, product in risk_score.products.items():
            for status in self.__get_product_status():
                if status.apply_condition(product.score) and self.__is_not_inelegible(product.status):
                    product.update_status(status.name)

    def __get_product_status(self):
        return self.product_status_builder.build_product_status_list()

    def __is_not_inelegible(self, status):
        return status != PRODUCT_SCORE_INELIGIBLE

    def fluub(self):
        return 100
