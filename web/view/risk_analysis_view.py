from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from application.use_case.risk_analysis_use_case import RiskAnalysisUseCase
from web.serializer.user_information_serializer import UserInformationSerializer


class RiskAnalysisView(APIView):
    user_information_serializer = None
    risk_analysis_use_case = None

    def __init__(self, risk_analysis_use_case=RiskAnalysisUseCase,
                 user_information_serializer=UserInformationSerializer):
        self.risk_analysis_use_case = risk_analysis_use_case
        self.user_information_serializer = user_information_serializer

    def post(self, request):
        user_information = self.user_information_serializer(data=request.data)

        if user_information.is_valid():
            response = self.risk_analysis_use_case.execute(user_information.data)
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(user_information.errors, status=status.HTTP_400_BAD_REQUEST)
