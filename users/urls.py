from django.urls import path
from django.contrib.auth import views as auth_views

from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="start-page/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="start-page/logout.html"), name="logout"),
    path('edit/', user_views.profile_edit, name="profile_edit"),
    path('<str:username>/follow', user_views.follow, name="follow"),
]
