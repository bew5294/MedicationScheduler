from .views import registration_view, login_view, logout_view
from django.urls import path

app_name = 'Auth'
urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout")
]