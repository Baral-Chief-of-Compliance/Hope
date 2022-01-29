from django.shortcuts import render
from .models import Post, MasterClass
from django.views.generic import View, ListView, DetailView


def index(request):
	return render (request, 'Sewing_site/home.html')


def about(request):
	return render (request, 'Sewing_site/about.html' )

class PostsView(ListView):
	model = Post
	queryset = Post.objects.all()
	template_name = "Sewing_site/post_list.html"


class PostDetails(DetailView):
	model = Post
	template_name = "Sewing_site/post_detail.html"


class MasterClassView(ListView):
	model = MasterClass
	queryset = MasterClass.objects.all()
	template_name = "Sewing_site/master_class_list.html"


class MasterClassDetails(DetailView):
	model = MasterClass
	template_name = "Sewing_site/master_class_detail.html"
