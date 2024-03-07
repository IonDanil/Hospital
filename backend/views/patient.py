from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from backend.mixin import HospitalGenericViewSet
from backend.serializers.patient import PatientListSerializer, PatientDetailedSerializer, \
    PatientCreateOrUpdateSerializer
from backend.models import Patient


# 12 Урок домашка

class PatientView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['first_name', 'last_name', ]
    filterset_fields = ['date_of_birth', 'gender']

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_patient', ]
        elif self.action == 'create':
            self.action_permissions = ['add_patient', ]
        elif self.action == 'update':
            self.action_permissions = ['change_patient', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_patient', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'retrieve':
            return PatientDetailedSerializer
        if self.action == 'create':
            return PatientCreateOrUpdateSerializer
        if self.action == 'update':
            return PatientCreateOrUpdateSerializer

    def get_queryset(self):
        return Patient.objects.all()