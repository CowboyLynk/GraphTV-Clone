import numpy as np
import json
import os
import django
import sys

# you have to set the correct path to you settings module
sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GraphTV.settings")
django.setup()

# import the django module
from imdb_database.models import Show, Season, Episode

# loads in the json files
with open('id_to_name_mapping.json', 'r') as f:
	id_to_name_mapping = json.loads(f.read())

with open('show_data.json', 'r') as f:
	db = json.loads(f.read())
request = None


for show in db:
	seasons = db[show]

	new_show = Show()
	new_show.show_id = show or "NONE"
	new_show.save()

	if not isinstance(seasons, dict):
		continue

	for season in seasons:
		episodes = db[show][season]

		new_season = Season()
		try:
			season_num = int(season)
		except ValueError:  # if the season doesn't have a number we can't use it, so don't save it
			continue
		new_season.season_num = season_num
		new_season.show = new_show
		new_season.save()

		if not isinstance(episodes, dict):
			continue

		for episode in episodes:
			episode = db[show][season][episode]
			title = episode.get("ep_title")
			ep_num = episode.get("ep_num")
			rating = episode.get("rating")
			num_ratings = episode.get("num_ratings")

			if not ep_num:  # if the episode doesn't have a number we can't use it, so don't save it
				continue

			new_episode = Episode()
			new_episode.title = title or "NONE"
			new_episode.ep_num = ep_num or -1
			new_episode.rating = rating or -1
			new_episode.num_ratings = num_ratings or -1.0
			new_episode.season = new_season
			new_episode.save()
