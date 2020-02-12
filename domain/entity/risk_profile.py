from domain.entity.risk_score import RiskScore


class RiskProfile:
    risk_score: RiskScore

    def __init__(self, risk_score: RiskScore):
        self.risk_score = risk_score

    def __eq__(self, other):
        return isinstance(other, RiskProfile) and \
               other.risk_score == self.risk_score
