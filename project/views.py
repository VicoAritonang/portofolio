from django.shortcuts import render
from .models import Project

# Create your views here.

def project_list(request):
    """
    View for listing all projects
    """
    projects = Project.objects.all()
    return render(request, 'project/project_list.html', {'projects': projects})
