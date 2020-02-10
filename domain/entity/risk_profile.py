class RiskProfile:
    risk_score = None

    def __init__(self, risk_score):
        self.risk_score = risk_score

    def __eq__(self, other):
        return isinstance(other, RiskProfile) and \
               other.risk_score == self.risk_score
