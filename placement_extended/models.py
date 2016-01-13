from django.db import models
from django.utils import timezone
from django import forms
from tinymce.models import HTMLField



class Post(models.Model):

	placement_year = models.CharField(max_length=200 , blank = True, null = True)
	Organization = models.CharField(max_length=200, blank = True, null = True)
	Date_of_visit = models.CharField(max_length=200, blank = True, null = True)
	No_of_offer= models.CharField(max_length=200, blank = True, null = True)
	compensation = models.CharField(max_length=200, blank = True, null = True)
	content = HTMLField()



















	upload = models.FileField(upload_to='uploads/placement_extended')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.placement_year
		
	
	

    	






    
# Create your models here.
