from rest_framework import serializers


class VehicleSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=True, min_value=0, max_value=9999)

