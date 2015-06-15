from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Coverpic(models.Model):
  url = models.CharField(max_length=200, blank=True)
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=200, default=None, null=True)
  image = models.ImageField(upload_to='coverpics/', null=True ,default=None)

  def __str__(self):
    return self.title

class Project(models.Model):
  title = models.CharField(max_length=200)
  description = RichTextField()
  shortDesc = models.CharField(max_length=200, default=None, null=True)
  image = models.ImageField(upload_to='projects/images/', default=None,blank=True, null=True)

  def __str__(self):
    return self.title
