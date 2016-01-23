from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

def college(request):
	posts = Post.objects.all()
	return render(request, 'campus/college.html', {'posts': posts})


def hostel(request):
	posts = Post.objects.all()
	return render(request, 'campus/hostel.html', {'posts': posts})


def labs(request):
	posts = Post.objects.all()
	return render(request, 'campus/labs.html', {'posts': posts})

	



    
    
    