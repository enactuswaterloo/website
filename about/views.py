from django.shortcuts import render
from about.models import Person

# Create your views here.
def index(request):
    people = Person.objects.filter(public=True)

    return render(request, "about/index.html", {"people": people})