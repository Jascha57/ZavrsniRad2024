from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('download_results/<int:reservation_id>/', views.download_results, name='download_results'),
    # Override the media url so that not everyone can access the private media files.
    path('media/private/<path:path>/<int:user_id>/<path:file_name>', views.hide_results, name='hide_results'),
    path('media/users/<path:path>/<path:file_name>', views.hide_profile_pictures, name='hide_profile_pictures'),
]