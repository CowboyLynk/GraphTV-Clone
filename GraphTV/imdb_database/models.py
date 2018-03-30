from django.db import models


class Show(models.Model):
	show_id = models.CharField(max_length=10, default="ERROR")


class Season(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	season_num = models.IntegerField()


class Episode(models.Model):
	season = models.ForeignKey(Season, on_delete=models.CASCADE)
	title = models.CharField(max_length=10, default="ERROR")
	ep_num = models.IntegerField()
	rating = models.FloatField()  # -1.0 if there are no ratings
	num_ratings = models.IntegerField()
