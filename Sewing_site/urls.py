from django.urls import path, include, re_path
from Sewing_site import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('post-list/', views.PostsView.as_view()),
    path('about-us/', views.about, name = 'about'),
]
