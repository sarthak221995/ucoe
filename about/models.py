from django.db import models
from django.utils import timezone

class Department(models.Model):
	about = models.TextField(blank=True, null = True)
	
	hod_text = models.TextField(blank=True, null = True)
	hod_image = models.ImageField(upload_to='images/about_images', blank=True, null = True) 
	
	created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
	modified = models.DateTimeField(auto_now=True,blank=True, null = True)


	def __unicode__(self):
		return self.hod_text