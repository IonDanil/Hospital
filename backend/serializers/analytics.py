
from rest_framework import serializers

class AnalyticsSerializer(serializers.Serializer):
    patient_count = serializers.IntegerField()
    doctor_count = serializers.IntegerField()
    visit_count = serializers.IntegerField()
