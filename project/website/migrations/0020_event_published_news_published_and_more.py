# Generated by Django 4.2.5 on 2024-03-15 19:57

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_schedule_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
