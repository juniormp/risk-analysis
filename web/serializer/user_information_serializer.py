from rest_framework import serializers
from domain.entity.person import MARITAL_STATUS


class UserInformationSerializer(serializers.Serializer):
    age = serializers.IntegerField(required=True, min_value=0)
    dependents = serializers.IntegerField(required=True, min_value=0)
    income = serializers.IntegerField(required=True, min_value=0)
    marital_status = serializers.ChoiceField(choices=MARITAL_STATUS, default='single')
    risk_question = serializers.ListField(child=serializers.BooleanField(), min_length=3, max_length=3)
    ownership_status = serializers.CharField()
    year_manufactured = serializers.IntegerField(required=True, min_value=0)
