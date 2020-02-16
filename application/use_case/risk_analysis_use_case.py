from application.use_case.abstract_use_case import AbstractUseCase
from domain.factory.risk_analysis_factory import RiskAnalysisFactory
from domain.service.risk_analysis_service import RiskAnalysisService


class RiskAnalysisUseCase(AbstractUseCase):
    def __init__(self, risk_analysis_service: RiskAnalysisService,
                 risk_analysis_factory: RiskAnalysisFactory):
        self.__risk_analysis_service = risk_analysis_service
        self.__risk_analysis_factory = risk_analysis_factory

    def execute(self, user_information):
        risk_analysis = self.__risk_analysis_factory.create_risk_analysis_from(user_information=user_information)
        self.__risk_analysis_service.apply_rules_on(risk_analysis=risk_analysis)
        risk_profile = self.__risk_analysis_service.get_result_from(risk_analysis.risk_profile)

        return risk_profile
