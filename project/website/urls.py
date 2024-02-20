from django.conf import settings
from django.urls import path, re_path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('news/', views.news, name='news'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)