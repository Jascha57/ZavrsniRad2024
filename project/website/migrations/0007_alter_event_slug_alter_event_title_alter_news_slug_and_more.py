# Generated by Django 5.0.2 on 2024-02-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_event_options_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(default='Title', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='Title', max_length=100, unique=True),
        ),
    ]
