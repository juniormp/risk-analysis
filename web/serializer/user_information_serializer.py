from rest_framework import serializers
from domain.entity.person import MARITAL_STATUS
from web.serializer.house_serializer import HouseSerializer
from web.serializer.vehicle_serializer import VehicleSerializer


class UserInformationSerializer(serializers.Serializer):
    age = serializers.IntegerField(required=True, min_value=0)
    dependents = serializers.IntegerField(required=True, min_value=0)
    income = serializers.IntegerField(required=True, min_value=0)
    marital_status = serializers.ChoiceField(choices=MARITAL_STATUS, default='single')
    risk_question = serializers.ListField(child=serializers.BooleanField(), min_length=3, max_length=3)
    house = HouseSerializer(required=False)
    vehicle = VehicleSerializer(required=False)

