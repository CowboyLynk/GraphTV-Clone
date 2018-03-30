from django.shortcuts import render
from django.http import HttpResponse
from .models import Show

import GetGraphData.main as p_data


# Create your views here.
def home(request):
	sid = request.GET.get("show_id")  # show id
	if not sid:
		return HttpResponse("nah fam")

	show = Show.objects.all().filter(show_id=sid)[0]
	seasons = show.season_set.all()

	episodes = []
	for season in seasons.order_by("season_num"):
		for episode in season.episode_set.all().order_by("ep_num"):
			episodes.append(episode)

	da_data = [
		[0, 67], [1, 88], [2, 77],
		[3, 93], [4, 85], [5, 91],
		[6, 71], [7, 78], [8, 93],
		[9, 80], [10, 82],[0, 75],
		[5, 80], [3, 90], [1, 72],
		[5, 75], [6, 68], [7, 98],
		[3, 82], [9, 94], [2, 79],
		[2, 95], [2, 86], [3, 67],
		[4, 60], [2, 80], [6, 92],
		[2, 81], [8, 79], [9, 83],
		[3, 75], [1, 80], [3, 71],
		[3, 89], [4, 92], [5, 85],
		[6, 92], [7, 78], [6, 95],
		[3, 81], [0, 64], [4, 85],
		[2, 83], [3, 96], [4, 77],
		[5, 89], [4, 89], [7, 84],
		[4, 92], [9, 98]]

	da_data, colors = p_data.get_data(episodes)

	return render(request, "home.html", {"show": show, "episodes": episodes, "da_data": da_data, "colors": colors})
