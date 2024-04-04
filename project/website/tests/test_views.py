from django.test import TestCase, Client
from django.urls import reverse

from website.views import *

class TestViews(TestCase):
    
        def setUp(self):
            self.client = Client()
            self.homepage_url = reverse('homepage')
            self.news_url = reverse('news')
            self.events_url = reverse('events')
            self.about_url = reverse('about')
    
        def test_homepage_GET(self):
            response = self.client.get(self.homepage_url)
    
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'homepage.html')
    
        def test_news_GET(self):
            response = self.client.get(self.news_url)
    
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'news.html')
    
        def test_events_GET(self):
            response = self.client.get(self.events_url)
    
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'events.html')
    
        def test_about_GET(self):
            response = self.client.get(self.about_url)
    
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'about.html')