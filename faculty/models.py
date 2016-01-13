from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    name = models.CharField(max_length=200,blank=True, null = True)
    qualification = models.CharField(max_length=200,blank=True, null = True)
    designation = models.CharField(max_length=200,blank=True, null = True)
    department = models.CharField(max_length=200,blank=True, null = True)
    area_of_specialization = models.CharField(max_length=200,blank=True, null = True)
    no_of_publication = models.CharField(max_length=200,blank=True, null = True)
    email_id = models.CharField(max_length=200,blank=True, null = True)
    mobile = models.CharField(max_length=200,blank=True, null = True)
    phd_student_guided = models.CharField(max_length=200,blank=True, null = True)
    mtech_student_guided = models.CharField(max_length=200,blank=True, null = True)
    photo = models.ImageField(upload_to='images',blank=True, null = True)
    upload = models.FileField(upload_to='faculty_t_cv/',blank=True, null = True)

    created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
    modified = models.DateTimeField(auto_now=True,blank=True, null = True)


    def __unicode__(self):
        return self.name

