from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('New_User', views.New_User, name='New_User'),
    path('Login', views.Login, name='Login'),
]