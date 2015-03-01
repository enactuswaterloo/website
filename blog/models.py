from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=250)
	featured_image = models.ImageField(upload_to='blog/images/', default=None, null=True)
	body = models.TextField()

	created_by = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
