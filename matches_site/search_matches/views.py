from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Team


# Create your views here.

def index(request):
    teams_list = Team.objects.order_by('name')
    context = {'teams_list': teams_list}
    return render(request, 'search_matches/index.html', context)


def detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'search_matches/detail.html', {'team': team})
