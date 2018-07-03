from django.shortcuts import render


def landing(request):
    """Landing Page. Cover Page, noth'n fancy
    """
    return render(request, 'landing/landing.html')


def home(request):
    """Home Page. Displays the Messages
    """
    return render(request, 'hole/home.html')
