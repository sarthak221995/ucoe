from django.shortcuts import render


def post_list(request):
    return render(request, 'highlights/hackoders.html', {})

def post_icrtc(request):
    return render(request, 'highlights/icrtc.html', {})
    # Create your views here.
