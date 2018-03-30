from django.shortcuts import render
from .models import Show, Season, Episode


# Create your views here.
def home(request):
	sid = request.GET.get("show_id")
	show = Show.objects.all().filter(show_id=sid)[0]
	seasons = show.season_set.all()

	episodes = []
	for season in seasons:
		for episode in season.episode_set.all():
			episodes.append(episode)

	return render(request, "home.html", {"show": show, "episodes": episodes})
