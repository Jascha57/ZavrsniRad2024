from django.shortcuts import render

from .models import *

def homepage(request):
    return render(request, 'homepage.html')

def news(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})