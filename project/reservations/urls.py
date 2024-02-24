from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)