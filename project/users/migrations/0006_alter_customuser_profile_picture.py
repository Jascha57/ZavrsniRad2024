# Generated by Django 4.2.5 on 2024-02-22 21:03

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default/user.jpg', upload_to=users.models.CustomUser.image_upload_to),
        ),
    ]
