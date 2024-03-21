from django.conf import settings
from django.urls import path, re_path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('news/', views.news, name='news'),
    path('news/<slug:slug>/', views.news_article, name='news_article'),
    path('events/', views.events, name='events'),
    path('events/<slug:slug>/', views.event, name='event'),
    path('about/', views.about, name='about'),
]