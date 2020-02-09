from web.serializer.user_information_serializer import UserInformationSerializer


class RiskAnalysisUseCase:
    def execute(self, request):
        risk_analysis = UserInformationSerializer(data=request.data)
        return [risk_analysis.is_valid(), risk_analysis.data]
