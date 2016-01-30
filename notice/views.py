from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.conf import settings


def post_list(request):
	posts = Post.objects.all()
	# posts.slide_image1 = settings.MEDIA_ROOT+posts.slide_image1

	return render(request, 'notice/e5.html', {'posts': posts})


def hackoders_list(request):
	posts = Post.objects.all()
	# posts.slide_image1 = settings.MEDIA_ROOT+posts.slide_image1

	return render(request, 'notice/hackoders.html', {'posts': posts})








