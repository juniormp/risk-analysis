from rest_framework import serializers


class HouseSerializer(serializers.Serializer):
    ownership_status = serializers.CharField(required=False)
