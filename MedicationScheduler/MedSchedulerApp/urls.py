from django.urls import path
from .views import home_view, front_view

app_name = 'MedicationScheduler'
urlpatterns = [
    path('', front_view, name="front"),
    path('home/', home_view, name='home')
]
