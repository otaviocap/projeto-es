from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('friends-home/', views.friends_home, name="friends-home"),
    path('profile/', views.profile_without_user, name="profile"),
    path('profile/<str:username>/', views.profile, name="profile"),
    path('posts/', views.post, name="post"),
    path('posts/<str:post_id>/like', views.like, name="like"),
    path('post/<str:post_id>/', views.single_post, name="single_post"),
]
