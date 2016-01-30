from django.shortcuts import render


def post_list(request):
    return render(request, 'highlights/hackoders.html', {})
    # Create your views here.
