from django.shortcuts import render

from main.models import Coverpic, Project

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def projects(request):
	projects = Project.objects.all()

	return render(request, "main/projects.html", {"projects": projects})

def sponsors(request):
    return render(request, "main/sponsors.html")

def contact(request):
    if request.method == 'POST':
    	if ('name' in request.POST and 'email' in request.POST and 'message' in request.POST) and (request.POST['name'] != "" and request.POST['email'] != "" and request.POST['message'] != ""):
    		if "@" not in request.POST['email'] or "." not in request.POST['email'] or len(request.POST['email']) < 5:
    			return render(request, "main/contact.html", {"error": "Invalid email entered."})
    		else:
	    		# Send email
	    		print "Sent email"
	    		return render(request, "main/contact.html", {"success": "success"})
    	else:
    		return render(request, "main/contact.html", {"error": "Not all fields have been filled out."})
    else:
    	return render(request, "main/contact.html")

