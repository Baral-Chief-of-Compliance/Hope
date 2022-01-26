from django.urls import path, include, re_path
from Sewing_site import views  

urlpatterns = [
    path('', views.index, name = "index"),
]