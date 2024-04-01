from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from backend.models import Schedule



class ScheduleSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ['id', 'timestamp_start', 'timestamp_end', 'doctor', 'duration']

    def get_duration(self, obj):
        return obj.duration()



class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['timestamp_start', 'timestamp_end', 'doctor']

    def validate(self, attrs, data):
        doctor = data.get('doctor')
        attrs = super().validate(attrs)

        timestamp_start, timestamp_end = attrs['timestamp_start'], attrs['timestamp_end']

        exists = Schedule.objects.filter(
            doctor=doctor,
            timestamp_start__lte=timestamp_start,
            timestamp_end__gte=timestamp_start
        ).exists()

        if exists:
            raise ValidationError('У нас есть накладка')

class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'timestamp_start', 'timestamp_end', 'doctor', 'duration']

    def get_duration(self, obj):
        return obj.duration()

class ScheduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"