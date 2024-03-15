from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404

from .models import *

def homepage(request):
    if request.user.is_staff:
        latest_news = News.objects.all().order_by('-date')[:3]
        latest_events = Event.objects.all().order_by('-date')[:3]
    else:
        latest_news = News.objects.filter(published=True).order_by('-date')[:3]
        latest_events = Event.objects.filter(published=True).order_by('-date')[:3]
    return render(request, 'homepage.html', {'latest_news': latest_news, 'latest_events': latest_events})

def news(request):
    search_query = request.GET.get('search', '')
    news = News.objects.annotate(
        full_name=Concat('author__first_name', Value(' '), 'author__last_name')
    ).filter(
        Q(title__icontains=search_query) |
        Q(short_description__icontains=search_query) |
        Q(full_name__icontains=search_query)
    ).order_by('-date')

    if not request.user.is_staff:
        news = news.filter(published=True)

    paginator = Paginator(news, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news.html', {'page_obj': page_obj})

def news_article(request, slug):
    if request.user.is_staff:
        article = News.objects.get(slug=slug)
    else:
        article = get_object_or_404(News, slug=slug, published=True)
    return render(request, 'news_article.html', {'article': article})

def events(request):
    search_query = request.GET.get('search', '')
    events = Event.objects.filter(
        Q(title__icontains=search_query) |
        Q(location__icontains=search_query) |
        Q(date__icontains=search_query)
    ).order_by('-date')

    if not request.user.is_staff:
        events = events.filter(published=True)

    paginator = Paginator(events, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'events.html', {'page_obj': page_obj})

def event(request, slug):
    if request.user.is_staff:
        event = Event.objects.get(slug=slug)
    else:
        event = get_object_or_404(Event, slug=slug, published=True)
    return render(request, 'event.html', {'event': event})