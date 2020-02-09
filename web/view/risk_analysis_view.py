from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from application.use_case.risk_analysis_use_case import RiskAnalysisUseCase


class RiskAnalysisView(APIView):
    risk_analysis_use_case = None

    def __init__(self, risk_analysis_use_case=RiskAnalysisUseCase):
        self.risk_analysis_use_case = risk_analysis_use_case

    def post(self, request):
        response = self.risk_analysis_use_case.execute(request, request)
        return Response(response, status=status.HTTP_200_OK)
