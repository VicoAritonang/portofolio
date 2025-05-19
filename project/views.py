from django.shortcuts import render
from supabase_client import supabase

def project_list(request):
    """
    View for listing all projects
    """
    # Fetch all projects from Supabase (tanpa order by id)
    response = supabase.table("project").select("*").execute()
    projects = response.data if response.data else []
    return render(request, "project/project_list.html", {"projects": projects})
