from django.shortcuts import render
from .models import Post, PostImage

def index(request):
	return render (request, 'Sewing_site/home.html')


