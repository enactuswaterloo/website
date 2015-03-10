from django.db import models

from django import forms
from django.contrib.auth.models import User

# Forms
class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Preferred first name', max_length=100, required=True)
    last_name = forms.CharField(label='Preferred last name', max_length=100, required=True)

    public = forms.BooleanField(initial=False, label="Display profile publicly?")

    program = forms.CharField(max_length=150, label="Program", required=False)
    year = forms.CharField(max_length=100, label="Year of graduation", required=False)
    picture = forms.ImageField(required=False)

    position = forms.ChoiceField(label="Team", required=True, choices=(
            ("Operations team", "Operations"),
            ("Finance team", "Finance"),
            ("Corporate relations", "Corporate relations"),
            ("Communications team", "Communications"),
            ("IT Team", "IT"),
            ("Environment team", "Environment"),
            ("Marketing team", "Marketing")
        ))
    bio = forms.CharField(widget=forms.Textarea, required=False)


# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, default=None, related_name="profile")

    priority = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="member-pics/", default=None, null=True, blank=True)

    program = models.CharField(max_length=150, default="Accounting and Financial Management")
    year = models.CharField(max_length=100, default="2019")

    position = models.CharField(max_length=100, default="Member")
    bio = models.TextField(blank=True, max_length=400) # Max lengths are unenforced for TextFields; that's intentional.

    def __str__(self):
    	return "%s %s" % (self.first_name, self.last_name)
