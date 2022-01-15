from django.contrib import admin
from .models import Medication, Prescription, Schedule, ScheduleElement

admin.site.register(Medication)
admin.site.register(Prescription)
admin.site.register(Schedule)
admin.site.register(ScheduleElement)
