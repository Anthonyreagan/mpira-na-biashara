# team/views.py
from django.shortcuts import render, get_object_or_404 # NEW: Import get_object_or_404
from .models import TeamMember

def team_list(request):
    members = TeamMember.objects.all()
    return render(request, 'team/team_list.html', {'members': members, 'title': 'Our Team'})

# NEW: Team Member Detail View
def team_detail(request, slug):
    member = get_object_or_404(TeamMember, slug=slug)
    return render(request, 'team/team_detail.html', {'member': member, 'title': member.name})