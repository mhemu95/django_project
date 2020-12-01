from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),
]
