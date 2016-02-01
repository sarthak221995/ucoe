from django.db import models



class Post(models.Model):
	YEAR_CHOICES = (('FIRSTSEMESTER','FIRST_SEMESTER'),('SECONDSEMESTER','SECOND_SEMESTER'),('THIRDSEMESTER','THIRD_SEMESTER'),('FOURTHSEMESTER','FOURTH_SEMESTER'),('FIFTHSEMESTER','FIFTH_SEMESTER'),('SIXTHSEMESTER','SIXTH_SEMESTER'),('SEVENTHSEMESTER','SEVENTH_SEMESTER'),('EIGHTSEMESTER','EIGHT_SEMESTER'),)
	PEOPLE_CHOICES = (('STUDENTS','STUDENTS'),('FACULTY','FACULTY'),)

	title = models.CharField(max_length=200, blank=True , null=True)
	upload = models.FileField(upload_to='uploads/', blank=True , null=True)
	people = models.CharField(max_length=20,choices=PEOPLE_CHOICES,blank=True, null = True)
	
	previous_year = models.CharField(max_length=20,choices=YEAR_CHOICES,blank=True, null = True)
	previous_year_title = models.CharField(max_length=200, blank=True , null=True)
	
	previous_year_upload = models.FileField(upload_to='uploads/', blank=True , null=True)

	time_table_year = models.CharField(max_length=20,choices=YEAR_CHOICES,blank=True, null = True)
	time_table_group = models.CharField(max_length=200, blank=True , null=True)
	time_table_upload = models.FileField(upload_to='uploads/', blank=True , null=True)


	syllabus_year = models.CharField(max_length=200, blank=True , null=True)
	syllabus_upload = models.FileField(upload_to='uploads/', blank=True , null=True)


	created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
	modified = models.DateTimeField(auto_now=True,blank=True, null = True)

	
	





	
    
    

    
    
    
	

   
# Create your models here.
