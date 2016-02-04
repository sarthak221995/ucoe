from django.db import models
from django.utils import timezone


class Post(models.Model):
    author_notice = models.CharField(max_length=200, blank = True, null = True)
    title_notice = models.CharField(max_length=200, blank = True, null = True)
    text_notice = models.TextField(blank = True, null = True)
    created_date_notice = models.DateTimeField(
            blank = True, null = True)
    link_notice = models.CharField(max_length=200, blank = True, null = True,default = "/#")         

    author_announcement = models.CharField(max_length=200, blank = True, null = True)
    title_announcement = models.CharField(max_length=200, blank = True, null = True)
    text_announcement = models.TextField(blank = True, null = True)
    created_date_announcement = models.DateTimeField(
            blank = True, null = True)
    link_announcement = models.CharField(max_length=200, blank = True, null = True,default = "/#")         



    event_title = models.CharField(max_length=200, blank = True, null = True)
    event_text = models.CharField(max_length=200, blank = True, null = True)
    event_image = models.ImageField(upload_to='images', blank=True, null = True)
    gallery_image =  models.ImageField(upload_to='images', blank=True , null = True)



    created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
    modified = models.DateTimeField(auto_now=True,blank=True, null = True)
    

    # def __unicode__(self):
    #     return self.modified
         
       
        
    


    


    


