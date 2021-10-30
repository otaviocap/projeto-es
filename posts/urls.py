from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('profile/', views.profile_without_user, name="profile"),
    path('profile/<str:username>/', views.profile, name="profile"),
    path('notifications/', views.profile, name="notifications"),
    path('posts/', views.post, name="post"),
    path('posts/<str:post_id>/like', views.like, name="post"),
]
