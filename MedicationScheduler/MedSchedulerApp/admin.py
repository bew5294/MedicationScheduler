from django.contrib import admin
from .models import *

admin.site.register(Medication)
admin.site.register(Presciption)
admin.site.register(Schedule)
admin.site.register(ScheduleElement)
