from django.urls import path

from . import views

app_name = 'MedicationScheduler'
urlpatterns = [
    # home page
    path('', views.home, name='home'),
    
    # login page (maybe in AuthApp)
    # path('/login', views.login, name='login'),
    
    # new prescription page
    path('new_precription', views.new_prescription, name='new_prescription'),
    
    # edit precription page
    # path('/precription/edit', views.edit_precription, name='edit_precription'),
    
    # new medication page
    path('new_medication', views.new_medication, name='new_medication'),
    
    # edit medication page
    # path('/medication/edit', views.edit_medication, name='edit_medication')
]

