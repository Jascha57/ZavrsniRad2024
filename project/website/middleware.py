from django.http import Http404
from django.urls import reverse

from .models import *

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_url = reverse('admin:index')
        if request.path.startswith(admin_url) and request.user.is_authenticated:
            if not request.user.is_superuser and not request.user.is_staff:
                raise Http404("Page not found")
        elif request.path.startswith(admin_url) and not request.user.is_authenticated:
            raise Http404("Page not found")
        response = self.get_response(request)
        return response


class ServicesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.services = Services.objects.all()[:5]
        response = self.get_response(request)
        return response
    

class NewsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.latest_news = News.objects.all().order_by('-date').filter(published=True)[:5]
        response = self.get_response(request)
        return response