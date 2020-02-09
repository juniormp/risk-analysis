from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from web.view.risk_analysis_view import RiskAnalysisView

urlpatterns = [
    path('risk', RiskAnalysisView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
