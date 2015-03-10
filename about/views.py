from django.shortcuts import render
from about.models import Person, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    people = Person.objects.filter(public=True, approved=True).order_by("-priority")

    return render(request, "about/index.html", {"people": people})

@login_required
def profile(request):
	if request.method != 'POST':
		return render(request, "about/member.html")

	# POST response to form
	if 'password' in request.POST:
		# Password changing
		if request.user.check_password(request.POST['oldpassword']):
			request.user.set_password(request.POST['password'])
		else:
			return render(request, "about/member.html", {error: "Incorrect password"})
	elif 'bio' in request.POST:
		person = Person.objects.get(user=request.user)
		if person == None:
			person = Person(user=request.user)

		# TODO: Complete