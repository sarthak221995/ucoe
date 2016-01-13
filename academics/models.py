from django.db import models



class Post(models.Model):


	text = models.CharField(max_length=200, blank = True, null = True)
	attachement = models.FileField(upload_to='uploads/academic', 
    	blank=True,default=None)
	created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
	modified = models.DateTimeField(auto_now=True,blank=True, null = True)


	def __unicode__(self):
		return self.text

   



