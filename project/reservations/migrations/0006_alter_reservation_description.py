# Generated by Django 4.2.5 on 2024-03-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_alter_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
