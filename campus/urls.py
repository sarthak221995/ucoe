from django.conf.urls import url
from . import views

urlpatterns = [
   # url(r'^$', views.post_list, name='post_list'),
   url(r'^college/$', views.college, name='college'),
   url(r'^hostel/$', views.hostel, name='hostel'),
   url(r'^labs/$', views.labs, name='labs'),
   

 
 
] 