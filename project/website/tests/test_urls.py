from django.test import SimpleTestCase
from django.urls import reverse, resolve

from website.views import *

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        # Sanity check to make sure the URL resolves to the correct view function
        # url = reverse('home')

        # The URL should resolve to the homepage view function
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, homepage)

    def test_news_url_resolves(self):
        url = reverse('news')
        self.assertEquals(resolve(url).func, news)

    def test_news_article_url_resolves(self):
        url = reverse('news_article', args=['some-slug'])
        self.assertEquals(resolve(url).func, news_article)

    def test_events_url_resolves(self):
        url = reverse('events')
        self.assertEquals(resolve(url).func, events)

    def test_event_url_resolves(self):
        url = reverse('event', args=['some-slug'])
        self.assertEquals(resolve(url).func, event)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)