from django.shortcuts import render, get_object_or_404

from blog.models import Post

# Create your views here.
def index(request):

	return render(request, "blog/index.html", {'posts': Post.objects.all()})

def detail(request, title):
	post = get_object_or_404(Post, title=title)
	return render(request, "blog/detail.html",
		{'post': post, 'subpageTitle': "Blog"})