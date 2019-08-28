from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.Category, name='category'),
     url(r'^Sell/$', views.Sell, name='Sell'),




]