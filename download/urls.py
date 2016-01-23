from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.post_list, name='post_list'),
   url(r'^previous_records/$', views.previous_records, name='previous_records'),
   url(r'^previous_records/(?P<previous_year>[A-Z]+)/$', views.post_summary, name='post_summary'),
   url(r'^time_table/$', views.time_table, name='time_table'),
   url(r'^time_table/(?P<time_table_year>[A-Z]+)/$', views.post_summary_tt, name='post_summary_tt'),
   url(r'^syllabus/$', views.syllabus, name='syllabus'),
   

 #
 
]