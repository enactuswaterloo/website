from django.shortcuts import render, get_object_or_404

from main.models import Coverpic, Project

# Create your views here.

def index(request):
    projects = Project.objects.all()[:3]
    coverpics = Coverpic.objects.all()

    return render(request, "main/index.html", {
      "projects": projects,
      "coverpics": coverpics
      })

def projects(request):
	projects = Project.objects.all()

	return render(request, "main/projects.html", {"projects": projects})

def project_details(request, project_id):
  project = get_object_or_404(Project, id=project_id)

  return render(request, "main/project_details.html", {"project": project})
