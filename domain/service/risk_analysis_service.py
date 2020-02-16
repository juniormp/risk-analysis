from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE
from domain.entity.product.status.product_status_builder import ProductStatusBuilder
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from array import array


class RiskAnalysisService:
    def __init__(self, product_status_builder: ProductStatusBuilder):
        self.product_status_builder = product_status_builder

    def apply_rules_on(self, risk_analysis: RiskAnalysis):
        for rule in risk_analysis.get_rules_list():
            rule.execute(risk_analysis)

    def get_result_from(self, risk_profile: RiskProfile):
        for __, product in risk_profile.get_products().items():
            for status in self.__get_product_status():
                if status.apply_condition(product.risk_score) and self.__is_not_inelegible(product.status):
                    product.update_status(status.name)

        return risk_profile

    def __get_product_status(self):
        return self.product_status_builder.build_product_status_list()

    def __is_not_inelegible(self, status):
        return status != PRODUCT_SCORE_INELIGIBLE
