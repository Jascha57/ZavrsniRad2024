# Generated by Django 4.2.5 on 2024-04-05 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_customuser_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='has_admin_access',
        ),
    ]
