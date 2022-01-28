from django.shortcuts import render
from .models import Post, PostImage
from django.views.generic import View


def index(request):
	return render (request, 'Sewing_site/home.html')


def about(request):
	return render (request, 'Sewing_site/about.html' )

class PostsView(View):

	def get(self, request):
		posts = Post.objects.all()
		return render(request, "Sewing_site/post_list.html", {"post_list": posts})
