from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('foods/new', views.addFood, name='addFood'),
    path('foods/<int:id>/update', views.updateFood, name='updateFood'),
    path('foods/<int:id>/delete', views.deleteFood, name='deleteFood'),

    path('profile/', views.profile, name='profile'),
    path('profile/new', views.createProfile, name='createProfile'),
    path('profile/<int:id>/update', views.updateProfile, name='updateProfile'),
    path('profile/<int:id>/delete', views.deleteProfile, name='deleteProfile'),

    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
