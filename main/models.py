from django.db import models

# Create your models here.

class Exec(models.Model):
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=150)

class Coverpic(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()