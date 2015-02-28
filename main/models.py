from django.db import models

# Create your models here.

class Person(models.Model):
    picture = models.ImageField(upload_to="member-pics/", default="member-pics/smiley_face.jpg")
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    program = models.CharField(max_length=150, default="Accounting and Financial Management")
    year = models.CharField(max_length=100, default="2019")

    position = models.CharField(max_length=100, default="Member")
    bio = models.TextField()

    def __str__(self):
    	return "{} {}, {}".format(self.firstName, self.lastName, self.program)

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
