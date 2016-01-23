from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    name = models.CharField(max_length=200,blank=True, null = True)
    
    designation = models.CharField(max_length=200,blank=True, null = True)
    email_id = models.CharField(max_length=200,blank=True, null = True)
    mobile = models.CharField(max_length=200,blank=True, null = True)

    created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
    modified = models.DateTimeField(auto_now=True,blank=True, null = True)


    def __unicode__(self):
        return self.name

