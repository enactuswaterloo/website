from django.shortcuts import render, get_object_or_404

from blog.models import Post

# Create your views here.
def index(request):

	return render(request, "blog/index.html", {'posts': Post.objects.all()})

def detail(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, "blog/detail.html",
		{'post': post, 'subpageTitle': "Blog"})