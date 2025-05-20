from django.shortcuts import render
from supabase_client import supabase

# Create your views here.
# nothing to do here
def award_list(request):
    """
    View for listing all awards and certifications
    """
    # Fetch all papers from Supabase
    response = supabase.table("paper").select("*").order("date", desc=True).execute()
    papers = response.data if response.data else []
    return render(request, 'award_and_certification/award_list.html', {'papers': papers})
