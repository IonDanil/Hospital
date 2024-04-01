
from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from backend.mixin import HospitalGenericViewSet
from backend.serializers.schedule import ScheduleListSerializer, ScheduleRetrieveSerializer, \
    ScheduleUpdateSerializer, ScheduleCreateSerializer
from backend.models import Schedule



class ScheduleView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # search_fields = ['first_name', 'last_name', ]
    # filterset_fields = ['date_of_birth', 'gender']

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_schedule', ]
        elif self.action == 'create':
            self.action_permissions = ['add_schedule', ]
        elif self.action == 'update':
            self.action_permissions = ['change_schedule', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_schedule', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        if self.action == 'retrieve':
            return ScheduleRetrieveSerializer
        if self.action == 'create':
            return ScheduleCreateSerializer
        if self.action == 'update':
            return ScheduleUpdateSerializer

    def get_queryset(self):
        return Schedule.objects.all()