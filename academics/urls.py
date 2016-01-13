from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^vision/$', views.vision, name='vision'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^$', views.post_list, name='post_list'),
]