from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^1/$', views.post_list, name='post_list'),
    url(r'^2/$', views.post_icrtc, name='post_icrtc'),
]