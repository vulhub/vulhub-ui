from rest_framework import serializers


class EnvironmentSerializer(serializers.Serializer):
    name = serializers.CharField()
    app = serializers.CharField()
    cve = serializers.CharField(allow_null=True)
    path = serializers.CharField()
    description = serializers.CharField(default='')
