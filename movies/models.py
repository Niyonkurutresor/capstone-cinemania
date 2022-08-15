from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Movies(models.Model):
	title = models.CharField(max_length=100)
	released_date = models.DateField(default=timezone.now)
	length_time = models.CharField(max_length=3)
	description = models.TextField()
	trail_link = models.URLField(max_length = 200)
	movies_image = models.ImageField()
	manager = models.ForeignKey(User, on_delete = models.CASCADE)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('movie-detail', kwargs={'pk': self.pk})
	