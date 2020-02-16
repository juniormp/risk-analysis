from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from application.use_case.risk_analysis_use_case import RiskAnalysisUseCase
from risk_analysis.service_registry import ServiceRegistry
from web.serializer.user_information_serializer import UserInformationSerializer


class RiskAnalysisView(APIView):
    def __init__(self):
        self.__risk_analysis_use_case = RiskAnalysisUseCase(ServiceRegistry.service_risk_analysis(),
                                                            ServiceRegistry.factory_risk_analysis())
        self.__user_information_serializer = UserInformationSerializer

    def post(self, request):
        user_information = self.__user_information_serializer(data=request.data)

        if user_information.is_valid():

            response = self.__risk_analysis_use_case.execute(user_information.data)
            return Response(response.to_array(), status=status.HTTP_200_OK)
        else:
            return Response(user_information.errors, status=status.HTTP_400_BAD_REQUEST)
