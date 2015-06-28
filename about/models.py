from django.db import models

from django import forms
from django.contrib.auth.models import User

# Forms
class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    program = forms.CharField(max_length=150, label="Program", required=True)
    year = forms.CharField(max_length=100, label="Expected Graduation Year", required=True)
    picture = forms.ImageField(label="Upload Picture (Suggested 1:1 height to width ratio)", required=False)

    link = forms.URLField(max_length=150, label="Personal link", required=False)
    link_type = forms.ChoiceField(label="Link type", required=True, choices=(
            ("Twitter", "Twitter"),
            ("Github", "Github"),
            ("LinkedIn", "LinkedIn"),
            ("Website", "Website"),
            ("Blog", "Blog"),
        ))

    position = forms.ChoiceField(label="Team", required=True, choices=(
            ("Communications", "Communications"),
            ("Finance", "Finance"),
            ("Fundraising", "Fundraising"),
            ("Graphic Designer", "Graphic Designer"),
            ("Human Resources", "Human Resources"),
            ("Marketing", "Marketing"),
            ("Social Media", "Social Media"),
            ("Sponsorship", "Sponsorship"),
            ("Webmaster", "Webmaster"),
            ("Iko Eco", "Iko Eco"),
            ("Project Cricket", "Project Cricket"),
            ("Project Spider", "Project Spider")
        ))
    bio = forms.CharField(label="Biography (140 characters limit)", widget=forms.Textarea, required=False, max_length=140)


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)

    position = forms.ChoiceField(label="Team", required=True, choices=(
            ("Communications", "Communications"),
            ("Finance", "Finance"),
            ("Fundraising", "Fundraising"),
            ("Graphic Designer", "Graphic Designer"),
            ("Human Resources", "Human Resources"),
            ("Marketing", "Marketing"),
            ("Social Media", "Social Media"),
            ("Sponsorship", "Sponsorship"),
            ("Webmaster", "Webmaster"),
            ("Iko Eco", "Iko Eco"),
            ("Project Cricket", "Project Cricket"),
            ("Project Spider", "Project Spider")
        ))


# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, default=None, related_name="profile")

    priority = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="member-pics/", default=None, null=True, blank=True)

    link_type = models.CharField(max_length=50, default=None, null=True, blank=True)
    link = models.URLField(max_length=150, default=None, null=True, blank=True)

    program = models.CharField(max_length=150)
    year = models.CharField(max_length=100)

    position = models.CharField(max_length=100, default="Member")
    bio = models.TextField(blank=True, max_length=140) # Max lengths are unenforced for TextFields; that's intentional.

    def __str__(self):
    	return "%s %s" % (self.user.first_name, self.user.last_name)
