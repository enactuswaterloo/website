from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=150)

    def __str__(self):
    	return "{}, {}".format(self.name, self.program)

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
