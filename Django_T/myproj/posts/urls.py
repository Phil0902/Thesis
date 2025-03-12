from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='posts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.posts_list, name='posts_list'),
]