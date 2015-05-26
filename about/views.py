from django.shortcuts import render
from about.models import Person, ProfileForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    people = Person.objects.filter(public=True, approved=True).order_by("-priority")

    return render(request, "about/index.html", {"people": people})

@login_required
def profile(request):

	if request.method != 'POST':
		initialDict = {
				'first_name': request.user.first_name,
				'last_name': request.user.last_name
			}
		try:
			initialDict.update({
				'program': request.user.profile.program,
				'year': request.user.profile.year,
				'position': request.user.profile.position,
				'bio':request.user.profile.bio,
				'public':request.user.profile.public,
				'link':request.user.profile.link
			})
		except:
			pass


		profileForm = ProfileForm(initial=initialDict)
		return render(request, "about/member.html", {"profileForm": profileForm})

	# POST response to form
	if 'password' in request.POST:
		# Password changing
		if request.user.check_password(request.POST['oldpassword']):
			request.user.set_password(request.POST['password'])
		else:
			return render(request, "about/member.html", {error: "Incorrect password"})
	elif 'first_name' in request.POST:
		profileForm = ProfileForm(request.POST, request.FILES)
		if profileForm.is_valid():

			person, created = Person.objects.get_or_create(user=request.user)

			request.user.first_name = profileForm.cleaned_data["first_name"]
			request.user.last_name = profileForm.cleaned_data["last_name"]
			request.user.save()

			person.program 	= profileForm.cleaned_data['program']
			person.public 	= profileForm.cleaned_data["public"]
			person.year 	= profileForm.cleaned_data["year"]
			person.position	= profileForm.cleaned_data["position"]
			person.bio 		= profileForm.cleaned_data["bio"]
			person.link 	= profileForm.cleaned_data["link"]

			if "picture" in request.FILES:
				person.picture = request.FILES["picture"]

			person.save()
		else:
			return render(request, "about/member.html", {"error": "Invalid input"})

	return HttpResponseRedirect("/team/")


def signup(request):

	if request.method != 'POST':
		signupForm = SignupForm()
		return render(request, "about/signup.html", {"form": signupForm})

	# POST response to form
	signupForm = SignupForm(request.POST)
	if signupForm.is_valid():

		username = signupForm.cleaned_data["username"]
		email = signupForm.cleaned_data["email"]
		password = signupForm.cleaned_data["password"]
		user = User.objects.create_user(username, email, password)

		user.first_name = signupForm.cleaned_data["first_name"]
		user.last_name = signupForm.cleaned_data["last_name"]
		user.save()

		person = Person(user=user)
		person.position	= signupForm.cleaned_data["position"]
		person.save()
	else:
		return render(request, "about/signup.html", {"error": "Invalid input", "signupForm": signupForm})

	return HttpResponseRedirect("/profile/edit")