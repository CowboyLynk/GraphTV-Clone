import numpy as np


def get_data(episodes):
	counter = 1
	data = []
	d_colors = []
	colors = ["#46B8AF", "#CE5858", "#5869CE", "#BD4EAC"]
	for episode in episodes:
		season_num = episode.season.season_num
		if episode.rating >= 0:
			entry = [counter, episode.rating, 'Rating: {}\nS{}E{} - {}\n'.format(episode.rating, episode.season.season_num, episode.ep_num, episode.title)]
			color = colors[season_num%len(colors)]
			entry.append("point { size: 5; fill-color: " + color + "; }")
			d_colors.append(colors[season_num%len(colors)])
			data.append(entry)
		counter += 1
	print(d_colors)
	return data, d_colors


