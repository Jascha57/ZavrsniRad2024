from django.shortcuts import render
from django.core.paginator import Paginator

from .models import *

def homepage(request):
    return render(request, 'homepage.html')

def news(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news.html', {'page_obj': page_obj})