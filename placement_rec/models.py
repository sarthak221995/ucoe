from django.db import models
from django.utils import timezone
from django.contrib import admin
from django import forms
from tinymce.models import HTMLField



class Post(models.Model):
    
    
    
   
    
    

    companies_logo =  models.ImageField(upload_to='uploads/placement-rec')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
    	return companies_logo
		




    
    
	


	


   