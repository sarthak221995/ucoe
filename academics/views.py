from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):

    posts = Post.objects.all()
    return render(request, 'academics/post_list.html', {'posts': posts})

def vision(request):
	return render(request, 'academics/vision.html', {})

def resources(request):

    posts = Post.objects.all()
    return render(request, 'academics/resources.html', {'posts': posts})

    
    