from django.shortcuts import render

from main.models import Exec, Coverpic

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def about_us(request):
    execs = Exec.objects.all()

    return render(request, "main/about_us.html", {"execs": execs})
