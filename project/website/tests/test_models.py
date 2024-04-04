import datetime
from django.test import TestCase
from django.utils import timezone

from users.models import CustomUser
from django.contrib.auth.models import Group
from website.models import News, Event, Services, Schedule

class TestModels(TestCase):
    
        # Set up some test data for testing the models
        def setUp(self):
            self.news1 = News.objects.create(
                title='News 1',
                description='Description 1',
                author=CustomUser.objects.create_user('testuser', 'password123'), 
            )
    
            self.event1 = Event.objects.create(
                title='Event 1',
                description='Description 1',
                location='Location 1',
                date=timezone.now(),
            )

            self.event2 = Event.objects.create(
                title='Event 2',
                description='Description 2',
                location='Location 2',
                date=timezone.now(),
                published=True,
            )

            self.service1 = Services.objects.create(
                title='Service 1',
                description='Description 1',
                duration=30,
            )
    
        # News and Events should automatically be assigned a slug on creation based on their title
        def test_news_is_assigned_slug_on_creation(self):
            self.assertEquals(self.news1.slug, 'news-1')
    
        def test_event_is_assigned_slug_on_creation(self):
            self.assertEquals(self.event1.slug, 'event-1')

        # News and Events should not be published by default
        def test_news_is_published(self):
            self.assertEquals(self.news1.published, False)

        def test_event_is_published(self):
            self.assertEquals(self.event1.published, False)
            # Check if the event is published if the published field is set to True
            self.assertEquals(self.event2.published, True)

        # When a service is created, a group should be created with the title + ' - Service'
        def test_service_is_group_created(self):
            group = Group.objects.filter(name=(self.service1.title + ' - Service'))
            self.assertTrue(group.exists())

        def test_service_schedule_created(self):
            schedules = Schedule.objects.filter(service=self.service1)

            # Check if the correct number of schedule entries are created
            expected_num_entries = (21 - 7) * 2  # Half-hour increments from 7:00 to 21:00
            self.assertEqual(schedules.count(), expected_num_entries)