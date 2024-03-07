import django_filters as filters
from backend.models import Doctor, Patient



class DoctorFilterSet(filters.FilterSet):
    first_name = filters.CharFilter(field_name='first_name')
    last_name = filters.CharFilter(field_name='last_name')
    specialization = filters.CharFilter(field_name='specialization')  # DOES NOT WORK!!

    class Meta:
        model = Doctor
        fields = {
            'last_name': ['exact', 'icontains'],
            'first_name': ['exact'],
            'specialization': ['exact']
        }

# class PatientFilterSet(filters.FilterSet):
#     first_name = filters.CharFilter(field_name='first_name')
#     last_name = filters.CharFilter(field_name='last_name')
#     date_of_birth = filters.DateFilter(field_name='date_of_birth')
#     gender = filters.CharFilter(field_name='gender')
#     contact_info = filters.CharFilter()
#
#     class Meta:
#         model = Patient
#         fields = {
#             'last_name': ['exact', 'icontains'],
#             'first_name': ['exact'],
#             'gender': ['exact'],
#             'date_of_birth': ['exact']
#         }