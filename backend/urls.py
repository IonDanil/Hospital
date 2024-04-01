from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import DoctorView, ServiceView, VisitView, PatientView, AnalyticsView, ScheduleView

urlpatterns = [
    path('schedule/',
        ScheduleView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'schedule/<int:id>/',
        ScheduleView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path('visit/<int:id>/rating/',
        VisitView.as_view({
            'put': 'set_rating'
        })
    ),
    path('analytics/',
         AnalyticsView.as_view({
             'get': 'get_analytics'
         })
    ),
    path('patient/',
        PatientView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'patient/<int:id>/',
        PatientView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 11 Урок домашка
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 9 Урок домашка > 10 Урок практика
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'doctor/<int:id>/',
        DoctorView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:id>/patient/',
        DoctorView.as_view({
            'get': 'list_patient'
        })
    ),
    path(
        'service/',
        ServiceView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'service/<int:id>/',
        ServiceView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'visit/',
        VisitView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'visit/<int:id>/',
        VisitView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    )
]
