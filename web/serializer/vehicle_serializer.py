from rest_framework import serializers


class VehicleSerializer(serializers.Serializer):
    year = serializers.DateField(input_formats=['%Y'])

