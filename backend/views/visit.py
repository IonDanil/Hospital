from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from backend.models import Visit
from backend.serializers.visit import VisitListSerializer, VisitCreateSerializer, VisitRetrieveSerializer, \
    VisitUpdateSerializer



class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'update':
            return VisitUpdateSerializer

    def get_queryset(self):
        return Visit.objects.all()