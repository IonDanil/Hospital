from django.contrib import admin
from django import forms

from .models import Specialization, Doctor, Service, Visit, Patient, Schedule


# 9 Урок домашка > 10 Урок практика
class DoctorAdminForm(forms.ModelForm):
    experience = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorAdmin(admin.ModelAdmin):
    form = DoctorAdminForm



admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialization)
admin.site.register(Service)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Schedule)