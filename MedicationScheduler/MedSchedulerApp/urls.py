from django.urls import path
from . import views

app_name = 'MedicationScheduler'
urlpatterns = [
    # front page
    path('', views.front, name="front"),
    
    # home page
    path('home', views.home, name='home'),
    
    # new prescription page
    path('new_prescription', views.new_prescription, name='new_prescription'),
    
    # edit prescription page
    # path('/prescription/edit', views.edit_prescription, name='edit_prescription'),
    
    # new medication page
    path('new_medication', views.new_medication, name='new_medication'),
    
    # edit medication page
    # path('/medication/edit', views.edit_medication, name='edit_medication')
]
