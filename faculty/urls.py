from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

    
    # url(r'^uploads/(?P<path>.*)$', views.post_detail, name='post_detail'),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

