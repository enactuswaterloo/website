from django.shortcuts import render
from about.models import Person

# Create your views here.
def index(request):
    people = Person.objects.filter(public=True, approved=True).order_by("-priority")

    return render(request, "about/index.html", {"people": people})

def member(request):
	return render(request, "about/member.html")