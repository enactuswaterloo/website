from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coverpic(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
    	return self.title

class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title
