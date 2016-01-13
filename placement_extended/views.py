from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Count



def post_list(request):
    posts = Post.objects.values('placement_year').annotate(dcount=Count('placement_year'))
    
    return render(request, 'placement_extended/post_list.html', {'posts': posts})


def post_detail(request, placement_year):
	posts = Post.objects.filter(placement_year=placement_year)
	# posts = get_object_or_404(Post, placement_year=placement_year)
	return render(request, 'placement_extended/post_detail.html', {'posts': posts})

    
    


def post_summary(request, placement_year,pk):
	pos = Post.objects.filter(placement_year=placement_year,pk=pk)
	#pos = Post.objects.all()
	return render(request, 'placement_extended/post_summary.html', {'pos': pos})
	#pos = get_object_or_404(Post, pk=pk)
	
    
    