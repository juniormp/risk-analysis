from domain.entity.product.status.product_status_builder import ProductStatusBuilder
from domain.entity.rule.asset_rules import AssetRules
from domain.entity.rule.person_rules import PersonRules
from domain.factory.risk_analysis_factory import RiskAnalysisFactory
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory
from domain.service.risk_analysis_service import RiskAnalysisService


class ServiceRegistry:
    @staticmethod
    def service_risk_analysis():
        return RiskAnalysisService(product_status_builder=ServiceRegistry.builder_product_status())

    @staticmethod
    def builder_product_status():
        return ProductStatusBuilder()

    @staticmethod
    def factory_risk_analysis():
        return RiskAnalysisFactory()

    @staticmethod
    def factory_risk_analysis_rules():
        return RiskAnalysisRulesFactory(person_rules=PersonRules(), asset_rules=AssetRules())

