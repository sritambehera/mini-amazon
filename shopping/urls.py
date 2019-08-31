
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^New_User/$', views.New_User, name='New_User'),
    url(r'^Login/$', views.Login, name='Login'),
    url(r'^Logout/$', views.Logout, name='Logout'),
    url(r'^SpecialOffers/$', views.SpecialOffers, name='SpecialOffers'),
    url(r'^ChangePassword/$', views.Change_Password, name='ChangePassword'),
    url(r'^Cart/$', views.Cart, name='Cart')
  #  url(r'^account/$', views.Account, name='account')
] 

urlpatterns += staticfiles_urlpatterns()