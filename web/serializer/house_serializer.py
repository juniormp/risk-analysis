from rest_framework import serializers


class HouseSerializer(serializers.Serializer):
    ownership_status = serializers.CharField(required=True, max_length=200)
