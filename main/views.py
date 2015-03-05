from django.shortcuts import render

from main.models import Coverpic, Project

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def projects(request):
	projects = Project.objects.all()

	return render(request, "main/projects.html", {"projects": projects})