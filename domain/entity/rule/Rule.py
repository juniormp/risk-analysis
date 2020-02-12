from abc import ABC, abstractmethod
from domain.entity.risk_analysis import RiskAnalysis


class Rule(ABC):
    @abstractmethod
    def execute(self, risk_analysis: RiskAnalysis):
        pass
