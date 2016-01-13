from django.db import models



class Post(models.Model):
    
    title = models.CharField(max_length=200, blank=True , null=True)
    
    

    upload = models.FileField(upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
    modified = models.DateTimeField(auto_now=True,blank=True, null = True)
	

   
# Create your models here.
