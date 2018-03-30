from django.shortcuts import render
from django.http import HttpResponse
from .models import Show

import GetGraphData.main as p_data


# Create your views here.
def home(request):
	sid = request.GET.get("show_id")  # show id
	if not sid:
		return render(request, "home.html")

	show = Show.objects.all().filter(show_id=sid)[0]
	seasons = show.season_set.all()

	episodes = []
	for season in seasons.order_by("season_num"):
		for episode in season.episode_set.all().order_by("ep_num"):
			episodes.append(episode)

	da_data = p_data.get_data(episodes)

	return render(request, "chart_page.html", {"show": show, "episodes": episodes, "da_data": da_data})
