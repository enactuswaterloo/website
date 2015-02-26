from django.db import models

# Create your models here.

class Person(models.Model):
    picture = models.CharField(max_length=100, default="smiley_face.jpg")
    name = models.CharField(max_length=100, default="N. Actus")
    program = models.CharField(max_length=100, default="Currently failing")
    year = models.CharField(max_length=100, default="2019")
    position = models.CharField(max_length=100, default="Member")
    bio = models.TextField(default="No description provided.")

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
