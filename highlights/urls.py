from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^1/$', views.post_list, name='post_list'),
    url(r'^2/$', views.post_icrtc, name='post_icrtc'),
    url(r'^3/$', views.post_call, name='post_call'),
    url(r'^4/$', views.post_gta, name='post_gta'),
    url(r'^5/$', views.post_date, name='post_date'),
    url(r'^6/$', views.post_contact, name='post_contact'),
    url(r'^7/$', views.post_reg, name='post_reg'),
    url(r'^8/$', views.post_comitte, name='post_comitte'),
   
]