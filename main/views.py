from django.shortcuts import render

from main.models import Person, Coverpic, Project

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def about_us(request):
    people = Person.objects.all()

    return render(request, "main/about_us.html", {"people": people})

def projects(request):
	projects = Project.objects.all()

	return render(request, "main/projects.html", {"projects": projects})

def blog(request):
	return render(request, "main/blog.html")