from django.shortcuts import render
from .models import Paper

# Create your views here.

def award_list(request):
    """
    View for listing all awards and certifications
    """
    papers = Paper.objects.all()
    return render(request, 'award_and_certification/award_list.html', {'papers': papers})
