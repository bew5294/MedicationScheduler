from django.urls import path
from .views import home_view, front_view

urlpatterns = [
    path('', front_view, name="front"),
    path('home/', home_view, name='home')
]
