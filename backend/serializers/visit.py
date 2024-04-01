from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from backend.models import Visit


class VisitRatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=10)

    def validate_rating(self, value):
        if self.instance.rating_set:
            raise ValidationError('Вы уже оставили оценку')


    class Meta:
        model = Visit
        fields = ['rating']


class VisitCreateSerializer(serializers.ModelSerializer):

    def validate_schedule(self, value):
        visit_count = value.visits.count()
        if 2 <= visit_count():
            raise ValidationError('Превышено максимальное количество мест')
        return value


    class Meta:
        model = Visit
        fields = ['patient', 'service', 'schedule']



class VisitListSerializer(serializers.Serializer):
    patient = serializers.CharField()
    service = serializers.CharField()
    status = serializers.CharField()
    schedule = serializers.CharField()

class VisitRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = "__all__"



class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['status']



