from rest_framework import serializers
from backend.models import Doctor

class DoctorListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    contact_info = serializers.CharField()
    id = serializers.IntegerField()

class DoctorRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"



class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'contact_info']

