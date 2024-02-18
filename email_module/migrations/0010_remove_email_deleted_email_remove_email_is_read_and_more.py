# Generated by Django 4.2.5 on 2023-11-22 05:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('email_module', '0009_email_deleted_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='deleted_email',
        ),
        migrations.RemoveField(
            model_name='email',
            name='is_read',
        ),
        migrations.AddField(
            model_name='email',
            name='deleted_by_user',
            field=models.ManyToManyField(blank=True, related_name='is_deleted_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='email',
            name='read_by_user',
            field=models.ManyToManyField(blank=True, related_name='is_read_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]