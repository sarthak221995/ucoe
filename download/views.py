from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'download/post_list.html', {'posts': posts})


def syllabus(request):
	posts = Post.objects.all()
	return render(request, 'download/syllabus.html', {'posts': posts})


def post_summary(request, previous_year):
	posts = Post.objects.filter(previous_year=previous_year)
	return render(request, 'download/post_summary.html', {'posts': posts})


def post_summary_tt(request, time_table_year):
	posts = Post.objects.filter(time_table_year=time_table_year)
	return render(request, 'download/post_summary_tt.html', {'posts': posts})



	
	
	
    
    


def previous_records(request):
	posts = Post.objects.values('previous_year').annotate(dcount=Count('previous_year'))
	return render(request, 'download/previous_records.html', {'posts': posts})


def time_table(request):
	posts = Post.objects.values('time_table_year').annotate(dcount=Count('time_table_year'))
	return render(request, 'download/time_table.html', {'posts': posts})
    
    
    