# Generated by Django 4.2.5 on 2024-03-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_event_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='duration',
            field=models.IntegerField(default=30, help_text='Duration in minutes'),
        ),
    ]
