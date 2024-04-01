from rest_framework import status
from rest_framework.response import Response


from backend.mixin import HospitalGenericViewSet
from backend.models import Doctor, Patient
from backend.service import get_upcoming_visits_count

class AnalyticsView(
    HospitalGenericViewSet
):
    def get_action_permissions(self):
        if self.action == 'get_analytics':
            self.action_permissions = []
    def get_analytics(self, request):
        response = {
            'patient_count': Patient.objects.all().count(),
            'doctor_count': Doctor.objects.all().count(),
            'visit_count': get_upcoming_visits_count()
        }
        return Response(status=status.HTTP_200_OK, data=response)

