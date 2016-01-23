from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'faculty_non_teaching/post_list.html', {'posts': posts})
   

# Create your views here.
