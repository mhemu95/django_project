from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^testlogin/$', views.my_login, name='testlogin'),
    url(r'^testpage/$', views.testpage, name='testpage'),
    url(r'^testlogout/$', views.my_logout, name='testlogout'),
]
