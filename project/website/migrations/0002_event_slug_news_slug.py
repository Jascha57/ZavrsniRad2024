# Generated by Django 5.0.2 on 2024-02-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='Event-Slug', unique=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='News-Slug', unique=True),
        ),
    ]
