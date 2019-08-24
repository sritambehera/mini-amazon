from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^New_User/$', views.New_User, name='New_User'),
    url(r'^Login/$', views.Login, name='Login'),
    url(r'^Logout/$', views.Logout, name='Logout'),
    url(r'^SpecialOffers/$', views.SpecialOffers, name='SpecialOffers'),
  #  url(r'^account/$', views.Account, name='account')
]