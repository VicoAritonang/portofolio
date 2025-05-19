from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    """
    View for the home page
    """
    return render(request, 'main/home.html')

def login_view(request):
    """
    View for the login page
    """
    return render(request, 'main/login.html')

@login_required
def profile(request):
    """
    View for the profile page (accessible only to logged in users)
    """
    return render(request, 'main/profile.html')
