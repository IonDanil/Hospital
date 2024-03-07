from rest_framework import serializers
from backend.models import Visit


class VisitListSerializer(serializers.Serializer):
    doctor = serializers.CharField()
    patient = serializers.CharField()
    service = serializers.CharField()
    visit_date_time = serializers.DateTimeField()
    status = serializers.CharField()

class VisitRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = "__all__"

class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"

class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['status', 'visit_date_time']
