from django.db import models
from django.utils import timezone

class Post(models.Model):
	gallery_college =  models.ImageField(upload_to='campus', blank=True , null = True)
	gallery_labs =  models.ImageField(upload_to='campus', blank=True , null = True)
	gallery_hostel =  models.ImageField(upload_to='campus', blank=True , null = True)

	created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
	modified = models.DateTimeField(auto_now=True,blank=True, null = True)









 

 

 
 	

 



  


# Create your models here.
