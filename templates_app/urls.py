from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("posts/", views.posts, name="posts"),
    path("profile_list/", views.profile_list, name="profile_list"),
]
