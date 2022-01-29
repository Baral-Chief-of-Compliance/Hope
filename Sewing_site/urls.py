from django.urls import path, include, re_path
from Sewing_site import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('post-list/', views.PostsView.as_view(), name = "post-list"),
    path('post-details/<int:pk>/', views.PostDetails.as_view(), name = "post-details"),
    path('about-us/', views.about, name = 'about'),
    path('master-class-list/', views.MasterClassView.as_view(), name = "master-class-list"),
    path('master-class-details/<int:pk>/', views.MasterClassDetails.as_view(), name = "master-class-detail")
]
