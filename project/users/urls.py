from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]