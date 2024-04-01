from rest_framework import serializers
from backend.models import Specialization


# 9 Урок домашка > 10 Урок практика
class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields = "__all__"
