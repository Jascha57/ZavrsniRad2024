# Generated by Django 4.2.5 on 2024-02-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(default='events/default.png', upload_to='events/'),
        ),
    ]
