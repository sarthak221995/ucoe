from django.shortcuts import render


def post_list(request):
    return render(request, 'highlights/hackoders.html', {})

def post_icrtc(request):
    return render(request, 'highlights/icrtc.html', {})

def post_date(request):
    return render(request, 'highlights/date.html', {})

def post_call(request):
    return render(request, 'highlights/call.html', {})


def post_gta(request):
    return render(request, 'highlights/gta.html', {})


def post_contact(request):
    return render(request, 'highlights/contact.html', {})


def post_reg(request):
    return render(request, 'highlights/reg.html', {})



    # Create your views here.
