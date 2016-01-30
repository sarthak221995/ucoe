from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/hackoders$', views.hackoders_list, name='hackoders_list'),
    url(r'^$', views.post_list, name='post_list'),
]