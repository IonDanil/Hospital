from rest_framework import serializers
from backend.models import Service


class ServiceListSerializer(serializers.Serializer):
    name = serializers.CharField()
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)

class ServiceRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"

class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['cost']
