from django.db import models

# Create your models here.

class Person(models.Model):

    public = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="member-pics/", default=None, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    program = models.CharField(max_length=150, default="Accounting and Financial Management")
    year = models.CharField(max_length=100, default="2019")

    position = models.CharField(max_length=100, default="Member")
    bio = models.TextField(blank=True, max_length=400) # Max lengths are unenforced for TextFields; that's intentional.

    def __str__(self):
    	return "%s %s" % (self.first_name, self.last_name)
